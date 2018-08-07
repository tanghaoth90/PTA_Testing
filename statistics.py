# -*- coding: utf-8 -*-'

# Author: Hao Tang
# Python 3.x

import csv
from collections import Counter

def clean_repr(scorerow):
	if scorerow[3] != "Normal":
		return tuple(scorerow[3:4])
	if scorerow[4] == "unsound":
		return tuple(scorerow[3:5])
	return tuple(scorerow[3:])

def print_counter(c):
	for e in c:
		print(str(e)+":"+str(c[e]))

if __name__ == "__main__":
	with open("score.csv", "r", encoding="gbk") as scorecsv:
		csvreader = csv.reader(scorecsv)
		scorerows = [scorerow[:] for scorerow in csvreader]
		benchmarks = set([scorerow[2] for scorerow in scorerows])
		for benchmark in benchmarks:
			print("Subject \""+benchmark+"\": ")
			homeworks = [[int(scorerow[0])]+scorerow[1:5]+[int(scorerow[5]),int(scorerow[6])] for scorerow in scorerows if scorerow[2]==benchmark]
			print("  %d projects received in total," % len(homeworks), end=" ")
			judge_statistics = Counter([clean_repr(scorerow) for scorerow in homeworks])
			#print_counter(judge_statistics)
			ft = lambda i, msg: sum([judge_statistics[e] for e in judge_statistics if len(e) > i and e[i] == msg])
			print("%d projects terminate normally, %d runtime error, %d timeout, %d no result;" 
				% (ft(0,'Normal'), ft(0,'Fail'), ft(0,'Timeout'), ft(0,'NoResult')))
			print("  Among %d normal projects, %d projects return sound results, and %d is unsound;" % (ft(0,'Normal'), ft(1,'sound'), ft(0,'Normal')-ft(1,'sound')))
			soundkeys = sorted([e for e in judge_statistics if len(e)==4])
			print("  The correct answer contains %d points-to relationships, while " % [scorerow[6] for scorerow in homeworks][0], end="")
			print(", ".join(["%d projects return %d" % (judge_statistics[e], e[2]) for e in soundkeys]), end=".\n\n")
