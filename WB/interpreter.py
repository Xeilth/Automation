import json
import webbrowser

output = ""
writeoutput = False
index = 0
urloutput = []

def writeout():
	write = open("output.txt", "w")
	write.write(output)
	write.close()
	try:
		inp
	except:	
		writestate = True
		print(f"Write State: {writestate}\n")
		return writestate
	writestate = "Success"
	print(f"Write State: {writestate}\n")
	return writestate

def add_data():
	with open("data.json", "r") as file:
		data = json.load(file)
	datadict = {}
	datalist = []
	datadict['name'] = input("Name:")
	datadict['url'] = input("Url:")
	datalist += data['list']
	datalist += [datadict]
	data['list'] = datalist
	uinp = input("Confirm?(y/n)")
	if str.lower(uinp) == "y":
		with open("data.json", "w") as file:
			json.dump(data, file, indent=8)
		del datadict
		del datalist
		del uinp
		loopbreak = True
		return loopbreak
	elif str.lower(uinp) == "n":
		print("Input Discarded\nTo Exit, Enter at Confirm.\n")
		del datadict
		del datalist
		del uinp
		loopbreak = False		
		return loopbreak
	else:
		loopbreak = True
		return loopbreak

with open("data.json", "r") as file:
	data = json.load(file)
	file.close()

for i in data['list']:
	output += f"{index}.Name: {i['name']}\n   Url: {i['url']}\n\n"
	urloutput += [i['url']]
	index += 1	

print(output)
if writeoutput:
	writeout()

inp = input("Press any key to exit.\n[w]To write output press\n[a]To add data\n[0]Enter index to open url.\n./>")
try:
	inp = int(inp)
except:
	if inp == "w":
		writeout()
		input(".")
	elif inp == "a":
		loopbreak = add_data()
		if not loopbreak:
			while loopbreak == False:
				loopbreak = add_data()
	exit()

try:
	webbrowser.open(urloutput[inp])
except:
	print("Invalid index.")
	input("Press any key to exit.")
