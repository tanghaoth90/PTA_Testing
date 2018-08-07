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
			print("["+benchmark+"]")
			judge_statistics = Counter([clean_repr(scorerow) for scorerow in scorerows if scorerow[2] == benchmark])
			print_counter(judge_statistics)
			print("")
			

			

