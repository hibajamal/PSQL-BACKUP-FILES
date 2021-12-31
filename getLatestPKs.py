import json
import math
import sys

backup = sys.argv[1]

backup = open(backup, "rb")

parsed = json.load(backup)

tables = []
maxKeys = {}

print("Looking across backup file for max PKs of all tables")

for obj in parsed:
	if obj["model"] not in tables:
		tables.append(obj["model"])
		maxKeys[obj["model"]] = obj["pk"]
	else:
		if obj["pk"] > maxKeys[obj["model"]]:
			maxKeys[obj["model"]] = obj["pk"]

print("Found all MAX keys! They are as follows:")

for key in maxKeys:
	print("Table:", key + ",", "Max PK:", maxKeys[key])

backup.close()