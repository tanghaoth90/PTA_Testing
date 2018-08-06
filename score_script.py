import subprocess, os

def get_result(filename):
	res = {}
	with open(filename, "r") as answer:
		for row in answer:
			row = row.strip()
			if not row: continue
			try:
				pt, objs = [t.strip() for t in row.split(":")]
				objs = set([int(t) for t in objs.split()])
				res[int(pt)] = objs
			except:
				pass
	return res

with open("resources/benchmark_info.txt", "r") as benchmark_info_file:
	for benchmark_name in benchmark_info_file:
		benchmark_name = benchmark_name.strip()
		if not benchmark_name: continue
		abbr_benchmark_name = benchmark_name.split(".")[-1]
		print("BM [%s]" % abbr_benchmark_name)
		stdAns = get_result("resources/standardAnswer/%s.stdout"%abbr_benchmark_name)
		print(stdAns)
		if os.path.isfile("result.txt"): os.remove("result.txt")
		subprocess.run(["java", "-jar", "analyzer.jar", "resources/finaltest", benchmark_name])
		userAns = get_result("result.txt")
		print(userAns)
