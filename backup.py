import sys
import json
import numpy as np 

master = sys.argv[1]
bckupF2 = sys.argv[2]

master = open(master, "rb")
f2 = open(bckupF2, "rb")

parsed1 = json.load(master)
parsed2 = json.load(f2)

print("\n#################################BACKUP PROCEDURE INITIATING#################################\n")
print("Master File loaded and being checked...\n\n")

print("\n\nLooking for new, modified and duplicate entries in new backup file...\n\n")

def printCount(i):
	if i%1000 == 0 and i>0:
		print(i, "entries scanned.")

new_entries = []
duplicates = 0
modified = []

count = 0
for item1 in parsed2[:10]: # new backup file
	flag = False
	for item2 in parsed1[:10]: # master file
		if item1["model"] == item2["model"] and item1["pk"] == item2["pk"]: # same reading spotted
			flag = True # do not add to new entries
			if item1 == item2:
				duplicates += 1
			else: # modified
				modified.append([item2, item1]) # [what it was, what it is]
		count += 1 

		printCount(count)
		count -= 1 # making sure print statement outside of loop is not executed as well
	
	if not flag:
		new_entries.append(item1)

	printCount(count)
	count += 1 # resetting count

print("Adding", len(new_entries), "entries in the master file...\n")

parsed1 += new_entries

print("Ignoring", duplicates, "duplicate entries.\n")

modify = ''

while True:
	modify = input(f"Modify {str(len(modified))} entries y/n? {modify}")
	print(modify)

	if modify == 'n':
		modify1 = ''
		modify1 = input(f"Are you sure you want to ignore all modifications (y/n)? The entries will remain in their original state. {modify1}")
		if modify1 == 'y':
			pass # do nothing, it will remain in parsed1
			break # do not ask again
		elif modify1 == 'n':
			pass # ask again
		else:
			print("Please enter either y for yes or n for no.") # ask again

	elif modify == 'y':
		modify2 = ''
		modify2 = input(f"Do you want to modify all without seeing them? {modify2}")
		if modify2 == 'y':
			for i in modified:
				parsed1[parsed1.index(i[0])] = i[1] # updated
			
			print("Updated!")
			break
			
		print("Showing all entries:\n")
		for i in modified:
			print("Original:", i[0], "\nNew:", i[1])
			update = ''
			while 1:
				update = input(f"Update? {update}")
				if update == 'y':
					parsed1[parsed1.index(i[0])] = i[1] # updated
					break
				elif update == 'n':
					parsed1 += [i[0]] # keep old
					break
				else: 
					print("Please enter either y for yes or n for no.") # ask again
		break
	else:
		print("Please enter either y for yes or n for no.") # ask again


print("\n\nWriting all entries into a file...")
# write to a new file
with open('data-compiled.json', 'w') as f:
    json.dump(parsed1, f, indent=None)

print("Written!")

f2.close()
master.close()