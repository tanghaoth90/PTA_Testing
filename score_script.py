# Author: Hao Tang
# Python 3.x

import subprocess, os, sys, time

def get_result(filename):
	res = {}
	try:
		with open(filename, "r") as answer:
			for row in answer:
				row = row.strip()
				if not row: continue
				try:
					pt, objs = [t.strip() for t in row.split(":")]
					objs = set([int(t) for t in objs.split() if int(t)>0]) # filter out extra "0"s
					res[int(pt)] = objs 
				except:
					pass
	except:
		pass
	return res

def compare_answer(stdans, userans):
	std_p2o = sum(len(stdans[pt]) for pt in stdans)
	user_p2o = sum(len(userans[pt]) for pt in userans)
	for pt in stdans:
		objs = stdans[pt]
		if pt not in userans:
			if len(objs) == 0: user_p2o += 0.2 # [punishment] no output about pointers that point to nothing
			else: return ("unsound", user_p2o, std_p2o)
		elif not objs.issubset(userans[pt]):
			return ("unsound", user_p2o, std_p2o)
	return ("sound", user_p2o, std_p2o)

def main(benchmark_info_file, stdans_dir, test_dir):
	test_logs = []
	with open(benchmark_info_file, "r") as benchmark_info_file:
		for benchmark_info in benchmark_info_file:
			benchmark_info = benchmark_info.strip()
			if not benchmark_info: continue
			benchmark_name, benchmark_timeout = benchmark_info.split()
			benchmark_timeout = int(benchmark_timeout)
			abbr_benchmark_name = benchmark_name.split(".")[-1]
			stdans = get_result(stdans_dir+"/%s.stdout"%abbr_benchmark_name)
			if os.path.isfile("result.txt"): os.remove("result.txt")
			runmsg = "Normal"
			start = time.time()
			try:
				subprocess.check_call(["java", "-jar", "analyzer.jar", test_dir, benchmark_name], 
					timeout=benchmark_timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			except subprocess.TimeoutExpired:
				runmsg = "Timeout"
			except:
				runmsg = "Fail"
			elapsed = int(time.time() - start)
			if runmsg == "Normal" and not os.path.isfile("result.txt"):
				runmsg = "NoResult"
			userans = get_result("result.txt")
			compare_stat = compare_answer(stdans, userans)
			#print("BM [%s] %s\n%s\n%s\n%s" % (abbr_benchmark_name, runmsg, str(stdans), str(userans), str(compare_stat)))
			print("[%s] %s %s %s %s, %d seconds" % (abbr_benchmark_name, runmsg, compare_stat[0], str(compare_stat[1]), str(compare_stat[2]), elapsed), flush=True)
			test_logs.append((abbr_benchmark_name, runmsg, compare_stat[0], compare_stat[1], compare_stat[2], elapsed))
	return test_logs

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3])