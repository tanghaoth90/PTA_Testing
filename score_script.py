with open("resources/benchmark_info.txt", "r") as benchmark_info_file:
	for benchmark_name in benchmark_info_file:
		benchmark_name = benchmark_name.strip()
		if benchmark_name:	
			print "BM[%s]" % benchmark_name
			with open("resources/standardOutput/%s.stdout"%benchmark_name, "r") as standardOutput:
				std_dict = {}
				for row in standardOutput:
					row = row.strip()
					if row:
						pt, objs = [t.strip() for t in row.split(":")]
						objs = set([int(t) for t in objs.split()])
						std_dict[int(pt)] = objs
				print std_dict
