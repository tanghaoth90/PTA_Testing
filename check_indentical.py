import sys, filecmp, os

pref = sys.argv[1]
for studir in os.listdir(pref):
	if os.path.isdir(pref+"/"+studir) and os.path.isfile(pref+"/"+studir+"/analyzer.jar"):
		if (filecmp.cmp(pref+"/"+studir+"/analyzer.jar", pref+"/pta-by-th.jar")):
			print(studir)
