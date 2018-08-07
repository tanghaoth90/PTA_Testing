# Author: Hao Tang
# Python 3.x

import subprocess, os, sys

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

def main():
	test_logs = []
	with open("../resources/benchmark_info_full.txt", "r") as benchmark_info_file:
		for benchmark_info in benchmark_info_file:
			benchmark_info = benchmark_info.strip()
			if not benchmark_info: continue
			benchmark_name, benchmark_timeout = benchmark_info.split()
			benchmark_timeout = int(benchmark_timeout)
			abbr_benchmark_name = benchmark_name.split(".")[-1]
			stdans = get_result("../resources/standardAnswer/%s.stdout"%abbr_benchmark_name)
			if os.path.isfile("result.txt"): os.remove("result.txt")
			runmsg = "Normal"
			try:
				subprocess.check_call(["java", "-jar", "analyzer.jar", "../resources/finaltest", benchmark_name], 
					timeout=benchmark_timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			except subprocess.TimeoutExpired:
				runmsg = "Timeout"
			except:
				runmsg = "Fail"
			if runmsg == "Normal" and not os.path.isfile("result.txt"):
				runmsg = "NoResult"
			userans = get_result("result.txt")
			compare_stat = compare_answer(stdans, userans)
			#print("BM [%s] %s\n%s\n%s\n%s" % (abbr_benchmark_name, runmsg, str(stdans), str(userans), str(compare_stat)))
			print("[%s] %s %s %s %s" % (abbr_benchmark_name, runmsg, compare_stat[0], str(compare_stat[1]), str(compare_stat[2])), flush=True)
			test_logs.append((abbr_benchmark_name, runmsg, compare_stat[0], compare_stat[1], compare_stat[2]))
	return test_logs

if __name__ == "__main__":
	main()