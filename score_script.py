# Author: Hao Tang
# Python 3.x

import subprocess, os

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

with open("resources/benchmark_info.txt", "r") as benchmark_info_file:
	for benchmark_info in benchmark_info_file:
		benchmark_info = benchmark_info.strip()
		if not benchmark_info: continue
		benchmark_name, benchmark_timeout = benchmark_info.split()
		benchmark_timeout = int(benchmark_timeout)
		abbr_benchmark_name = benchmark_name.split(".")[-1]
		stdAns = get_result("resources/standardAnswer/%s.stdout"%abbr_benchmark_name)
		if os.path.isfile("result.txt"): os.remove("result.txt")
		runmsg = "Normal"
		try:
			subprocess.run(["java", "-jar", "analyzer.jar", "resources/finaltest", benchmark_name], 
				timeout=benchmark_timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		except subprocess.TimeoutExpired:
			runmsg = "Timeout"
		except:
			runmsg = "Fail"
		if runmsg == "Normal" and not os.path.isfile("result.txt"):
			runmsg = "NoResult"
		userAns = get_result("result.txt")
		print("BM [%s] %s\n%s\n%s" % (abbr_benchmark_name, runmsg, str(stdAns), str(userAns)))
