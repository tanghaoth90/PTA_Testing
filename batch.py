# -*- coding: utf-8 -*-'

# Author: Hao Tang
# Python 3.x

import sys, os, shutil, csv, datetime
from collections import Counter
import score_script

def printFlush(s):
	print(s, flush=True)

if __name__ == "__main__":
	pref = sys.argv[1]
	tot_hw, valid_hw = 0, 0
	status_counter = Counter()
	with open("score.csv", "w", encoding="gbk") as csvfile:
		csvwriter = csv.writer(csvfile)
		printFlush(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		printFlush("")
		for studir in os.listdir(pref):
			if not os.path.isdir(pref+"/"+studir): continue
			analyzer_jar = pref+"/"+studir+"/analyzer.jar"
			tot_hw += 1
			if (os.path.isfile(analyzer_jar)):
				printFlush("Testing homework #%d: %s"%(tot_hw, studir))
				valid_hw += 1		
				if os.path.isfile("analyzer.jar"): os.remove("analyzer.jar")
				shutil.copy2(analyzer_jar, "analyzer.jar")
				test_log = score_script.main(sys.argv[2], sys.argv[3], sys.argv[4])
				status_counter[test_log[0][1:3]] += 1
				for slog in test_log:
					csvwriter.writerow([tot_hw, studir] + list(slog))
			else:
				printFlush("Missing homework #%d: %s"%(tot_hw, studir))
			printFlush(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			printFlush("")
		printFlush("\n*********\nSummary:\nValid homework: %d out of %d" % (valid_hw, tot_hw))
		for key in status_counter:
			printFlush("Valid Status %s: %d"%(str(key),status_counter[key]))
