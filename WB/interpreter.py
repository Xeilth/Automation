import json
import webbrowser
import time
import os

writeoutput = False
spacing = "___________________________________________________________________________________________"
emptyjson = {"list": []}
defaultdata = '{"list":[{"name": "Google", "url": "https://www.google.com"}]}'
loop = True
max_eocreach = 50
eocreach = 0

def dataerror():
		file = open("data.json", "w")
		file.write(defaultdata)
		file.close()
		print("Decoding Error, are you perhaps new?(y/n)")
		ans = input("Answer:").lower()
		if ans == "y":
			print("As a Guide you can see the help menu below.\n")
			helpmenu()
			exit()
		elif ans == "n":
			print("Have fun using me again :)\n Restarting maybe needed.")
			input("")
			exit()

def data_backup():
	with open("data.json", "r") as currdata:
		backupdata = json.load(currdata)
	with open("databackup.json", "w") as backup:
		json.dump(backupdata, backup, indent=4)
	currdata.close()
	backup.close()
	del backupdata
	return

def load_data():
	try:
		del output, index, urloutput, data,
	except UnboundLocalError:
		#print("Unbound Local Error")
		pass
	output = ""
	index = 0
	urloutput = []
	try:
		with open("data.json", "r") as file:
			data = json.load(file)
			file.close()
	except:
		dataerror()
		exit()
	try:
		for i in data['list']:
			output += f"{index}.Name: {i['name']}\n   Url: {i['url']}\n\n"
			urloutput += [i['url']]
			index += 1
	except TypeError:
		os.remove("./data.json")
	return data, output, urloutput, index

def helpmenu():
	os.system("cls")
	print("-----Help Menu-----")
	print("\nMain:")
	print("Press any key to exit.\n[w]To write output\n[a]To append data\n[e]To edit data\n[0]Enter index to open url.\n[h]For help.")
	print("\nedit data function:")
	print("[a] To access append data function\npop <item index> to remove the item at the specified index.\n revert to revert to databackup.")
	print("\nadd data function:")
	print("Press any key at confirm prompt to exit.")
	print("-------------------")
	return

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
	os.system("cls")
	print(f"{spacing}\n--Append Data--\n----------")
	print("-New Item-")
	datadict = {}
	datalist = []
	datadict['name'] = input("Name:")
	datadict['url'] = input("Url:")
	originaldata = data['list']
	datalist += data['list']
	datalist += [datadict]
	data['list'] = datalist
	print(spacing)
	print("\nNew List :\n\n")
	newlist = ""
	index = 0
	for a in data['list']:
		newlist += f"{index}.Name: {a['name']}\n   Url: {a['url']}\n\n"
		index += 1
	print(newlist)
	print(spacing)
	uinp = input("Confirm?(y/n)")
	if str.lower(uinp) == "y":
		data_backup()
		with open("data.json", "w") as file:
			json.dump(data, file, indent=4)
		del datadict, datalist, uinp
		loopbreak = True
	elif str.lower(uinp) == "n":
		print("Changes Discarded\nTo Exit, Enter at Confirm.\n")
		del datadict, datalist, uinp
		data['list'] = originaldata
		loopbreak = False
	else:
		loopbreak = True
		del datadict, datalist, uinp
		data['list'] = originaldata
	return loopbreak

def edit_data():
	os.system("cls")
	print(f"\n{spacing}\nEdit Data\n----------\nList Right Now:")
	print(output)
	print(spacing)
	print("-Remove-\nTo remove an item, type \"pop <item index>\" without <>.")
	print("To remove all item, type \"pop all\"\n")
	print("-Revert-\nTo revert to backup data, type \"revert\" with no parameters\n")
	uinp = input(">")

	if uinp.lower() == "a":
		add_data()
	try:
		action, parameter = uinp.split(" ", 1)
		action = action.lower()

		# Actions With Parameter Needs

		if action == "pop":
			try:
				idx = int(parameter)
				with open("data.json", "r") as file:
					data = json.load(file)
					try:
						data['list'].pop(idx)
					except IndexError:
						print("Invalid Index.")
				print("\nNew List :\n\n")
				newlist = ""
				index = 0
				for a in data['list']:
					newlist += f"{index}.Name: {a['name']}\n   Url: {a['url']}\n\n"
					index += 1
				print(newlist)
				print(spacing)
				inp = input("Confirm?(y/n)").lower()
				if inp == "y":
					data_backup()
					with open("data.json", "w") as file:
						json.dump(data, file, indent=4)
				elif inp == "n":
					print("Change Discarded\nTo Exit, Press enter at Confirm.\n")
				del action, idx, inp, newlist
			except:
				if parameter.lower() == "all":
					print("Are you sure to do this action [pop all] and remove all items?")
					inp = input("Confirm?(y/n)").lower()
					if inp == "y":
						print("Removing all items.")
						with open("data.json", "w") as file:
							json.dump(emptyjson, file, indent=4)
						print("Proccess Success. Returning in 5 seconds.")
						time.sleep(5)
						return
					elif inp == "n":
						print("Action abort. \nReturn in 5 seconds.")
						time.sleep(5)
						return
					print("Pop All Here.")
				return
	except ValueError:
		action = uinp
		action = action.lower()

		# Actions Without The Needs of Parameter

		if action == "revert" or action == "r":
			try:
				with open("databackup.json", "r") as backupfile:
					backup = json.load(backupfile)
					backupfile.close()
					index = 0
					backuplist = ""
					for a in backup['list']:
						backuplist += f"{index}.Name: {a['name']}\n   Url: {a['url']}\n\n"
						index += 1
					print(f"Backup Data : \n{backuplist}")
					print("Backup file found, do you want to revert back to it?(y/n)")
					print("Note: Be Careful reverting means overwriting the current data.")
					inp = input(">").lower()
					if inp == "y":
						print("Reverting back to backup...")
						with open("data.json", "w") as file:
							json.dump(backup, file, indent=4)
							file.close()
						print("\nRevert Success!\nReturn in 5 seconds.")
						time.sleep(5)
						return
					elif inp == "n":
						print("Going Back to main menu.")
						return
					else:
						input("Invalid Input")
						exit()
			except FileExistsError or FileNotFoundError:
				print("You don't have any auto created backup.\nBackup will be created everytime you edit the data in through this code.")

		else:
			print("Invalid Syntax.")

	
# ------------------------ End of functions ----------------------------
while loop:
	if eocreach == max_eocreach-1:
		loop = False
	data, output, urloutput, index = load_data()
	os.system("cls")
	print(f"List:\n{output}")
	if output == "":
		print("Your List Is Empty, Consider Adding Something Here :(")
	if writeoutput:
		writeout()
	print("Press any key to exit.\n[h]For help.")
	print("[w]To write output\n[a]To append data\n[e]To edit data\n[0]Enter index to open url.")
	inp = input(f"EOC:{eocreach}./>")
	try:
		inp = int(inp)
		try:
			webbrowser.open(urloutput[inp])
		except ValueError:
			print("Invalid index.")
			input("Press any key to exit.")
	except ValueError:
		inp = str.lower(inp)
		if inp == "w":
			writeout()
			input(".")
		elif inp == "a":
			loopbreak = add_data()
			while not loopbreak:
				loopbreak = add_data()
		elif inp == "e":
			edit_data()
		elif inp == "h" or inp == "help":
			helpmenu()
			input("Press any key to return.")

	eocreach += 1
	print("\n\n\n")
print(f"Woah! {max_eocreach} Loops? You are very dedicated!\nTime to stop though :)")
time.sleep(5)