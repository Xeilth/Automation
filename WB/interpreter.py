import json
import webbrowser
import time
import os

writeoutput = False
spacing = "___________________________________________________________________________________________"
spacing_dash = "-------------------------------------------------------------------------------------------"
emptyjson = {"list": []}
defaultdata = '{"list":[{"name": "Google", "url": "https://www.google.com"}]}'
loop = True
max_eocreach = 50
eocreach = 0
exitafteropenurl = True
recent_action = ""
exportfolder = "export"
seperator = [", ", ","]

dataname = "data.json"
backupdataname = "databackup.json"


def dataerror():
		file = open(dataname, "w")
		file.write(defaultdata)
		file.close()
		print("Decoding Error, are you perhaps new?(y/n)")
		ans = input("Answer:").lower()
		if ans == "y":
			print("As a Guide you can see the help menu below.\n")
			generalhelp = "help"
			helpmenu(generalhelp)
			input("\n\nPress any key to exit.")
			exit()
		elif ans == "n":
			print("Have fun using me again :)\nPress any key to return.")
			input("")
			time.sleep(2)
			return


def data_backup():
	with open(dataname, "r") as currdata:
		backupdata = json.load(currdata)
	with open(backupdataname, "w") as backup:
		json.dump(backupdata, backup, indent=4)
	currdata.close()
	backup.close()
	del backupdata
	return


def load_data():
	output = ""
	urloutput = []
	try:
		with open(dataname, "r") as file:
			data = json.load(file)
			file.close()
	except:
		dataerror()
		exit()
	try:
		for ind, i in enumerate(data['list']):
			output += f"{ind}.Name: {i['name']}\n   Url: {i['url']}\n\n"
			urloutput += [i['url']]
	except TypeError:
		os.remove(f"./{dataname}")
		act = "Reset data."
		return data, output, urloutput, act
	return data, output, urloutput


def helpmenu(command):
	os.system("cls")
	try:
		command.lower()
		cmdname = command.split(" ", 1)[1]
		# Help - Open Url Command
		try:
			cmdname = int(cmdname)
			if not cmdname == 0:
				helpmenu("help 0")
				return
		except ValueError:
			pass

		''' Command Detail Template
		# Help - name Command
		elif cmdname == "name":
			title = "Help > name Command"
			print(title)
			print("command details")
			print(spacing[0:len(title)])
			input("Press any key to return.")
		'''

		# Help - Help Command
		if cmdname == "help":
			title = "Help > Help Command"
			print(title)
			print("Help menu can be accessed with [h] or [help].\n")
			print("Syntax: help <commandname>")
			print("if used without argument, will take you to the general help menu.")
			print("commandname argument is optional, only used to view details and arguments of specified command.")
			print(spacing_dash[0:len(title)])
			input("Press any key to return.")

		# Help - Export Command
		elif cmdname == "export":
			title = "Help > Export Command"
			print(title)
			print("Export Command is used to export current data into text and json format.")
			print(f"Exported data is stored at {exportfolder} folder inside the module directory.")
			print("Export command doesn't take in any arguments.")
			print("Syntax: export")
			print(f"\nAuto-Export : {writeoutput}")
			print(f"Export Folder : {exportfolder}")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Open Url Command
		elif cmdname == 0:
			title = "Help > Open Url Command"
			print(title)
			print("This command open the url of the specified item.")
			print("This command can be accessed with any item index available inside the list.")
			print("This command doesn't have a prefix or command name.")
			print("Please mind that item index starts from 0 not 1\nIf Index exceeds list, returns error.")
			print("Syntax: 0")
			print(f"\nExit After Url Is Open : {exitafteropenurl}")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Add Command
		elif cmdname == "add" or cmdname == "append":
			title = "Help > Add Command"
			print(title)
			print("Add command Adds new item into existing data.")
			print("Add command can be accessed with [a], [add], and [append].")
			print("Syntax: Add <name>, <url>")
			print("Ex: Add Google, https://www.google.com")
			print("Add command requires both name and url arguments.\nIf called without argument returns error.")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Insert Command
		elif cmdname == "ins" or cmdname == "insert":
			title = "Help > Insert Command"
			print(title)
			print("Insert command inserts new item into specified index on existing data.")
			print("Insert command can be accessed with [ins] and [insert].")
			print("Syntax: Insert <destination index> <name>, <url>")
			print("Ex: Insert 5 google, https://www.google.com")
			print("This line will place the item into index 5 and the original index 5 is moved to index 6.")
			print("Insert command requires all three of the listed arguments.")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Replace Command
		elif cmdname == "rep" or cmdname == "replace":
			title = "Help > Replace Command"
			print(title)
			print("Replace command replaces an item with another item but keeping the original item.")
			print("Replace command can be accessed with [rep] and [replace].")
			print("Syntax: Replace <origin index> <destination index>")
			print("Ex: Replace 5 0")
			print("This command will replace index 0 with index 5, index 0 will be pushed to index 1")
			print("Replace command requires both destination and origin arguments.")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Remove Command
		elif cmdname == "remove" or cmdname == "rmv" or cmdname == "pop" or cmdname == "rem":
			title = "Help > Remove Command"
			print(title)
			print("Remove command removes the specified item.")
			print("Remove command can be accessed with [remove], [rmv], and [pop]")
			print("Syntax: remove <item index>")
			print("Remove command requires the item index argument.\nIf not given, returns an error.")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		# Help - Revert Command
		elif cmdname == "revert" or cmdname == "restore" cmdname == "rev":
			title = "Help > Revert Command"
			print(title)
			print("Revert command revert the current data to the backup data.")
			print("If there is no backup data, it will not change your data.")
			print("Revert command is accessed with [revert], [rev], and [restore]")
			print("Syntax: revert")
			print("Revert command doesn't take any arguments.")
			print(spacing[0:len(title)])
			input("Press any key to return.")

		else:
			print("Invalid Command Name.\nFor reference, please check the help menu.")
			input("Press any key to return")
		return
	except IndexError:
		pass
	except ValueError:
		pass	

	#General Help Menu
	print("-----Help Menu-----")
	# First print for General commands
	print("[help]To show this help menu.\n[export]To Export List\n[0]Enter index to open url.")
	# Second print for data editing commands
	print("[add]To add data\n[insert]To insert data\n[replace]To replace data")
	print("[remove]To remove data\n[revert]To revert to backup")
	# Third print for notes and similar things
	print("Type 'help <command name>' without the <> for command details.")
	return


def export_data(foldername):
	try:	
		t = time.localtime()
		currtime = time.strftime("%d-%m-%y %H.%M.%S", t)
		write = open(f"./{foldername}/{currtime}-list.txt", "w")
		write.write(output)
		with open(f"./{foldername}/{currtime}-data.json", "w") as file:
			json.dump(data, file, indent=4)
			file.close()
		write.close()
		
		try:
			inp
			writestate = "Success"
		except:
			writestate = True
		print(f"Write State: {writestate}\n")
		act = "Export data."
		return act
	except FileNotFoundError:
		os.system(f'md "{foldername}"')
		return export_data(foldername)


def add_data(item_info):
	try:
		os.system("cls")
		_, item_info = item_info.split(" ", 1)
		try:
			item_name, item_url = item_info.split(", ", 1)
		except:
			item_name, item_url = item_info.split(",", 1)
		datadict = {'name': item_name, 'url': item_url}
		data['list'].append(datadict)
		data_backup()
		with open(dataname, "w") as file:
			json.dump(data, file, indent=4)
		del datadict
		act = "Added an item to the list."
		return act
	except ValueError:
		print("Required Arguments: Name, Url.")
		input("Press any key to return.")
	return


def insert_data(cmd_info):
	try:
		os.system("cls")
		_, cmd_info = cmd_info.split(" ", 1)
		index, item_info = cmd_info.split(" ", 1)
		try:
			item_name, item_url = item_info.split(", ", 1)
		except:
			item_name, item_url = item_info.split(",", 1)
		datadict = {'name': item_name, 'url': item_url}
		data['list'].insert(int(index), datadict)
		data_backup()
		with open(dataname, "w") as file:
			json.dump(data, file, indent=4)
		del datadict
		act = "Inserted an item to the list."
		return act
	except ValueError:
		print("Required Arguments: Destination Index, Name, Url.")
		input("Press any key to return.")
	return


def replace_data(cmd_info):
	try:
		_, origin, destination = cmd_info.split()

		with open(dataname, "r") as file:
			data = json.load(file)
			try:
				datadict = data['list'][int(origin)]
				data['list'].pop(int(origin))
				data['list'].insert(int(destination), datadict)
				data_backup()
				with open(dataname, "w") as file:
					json.dump(data, file, indent=4)
				act = "Replaced an item."
				return act
			except IndexError:
				print("Invalid Index.\nReturn in 2 seconds.")
				time.sleep(2)
				return
	except ValueError:
		print("Required Arguments: Destination Index, Origin Index.")
		input("Press any key to return.")
	return


def remove_data(parameter):
	try:
		_, parameter = parameter.split()
		with open(dataname, "r") as file:
			data = json.load(file)
			try:
				data['list'].pop(int(parameter))
				data_backup()
				with open(dataname, "w") as file:
					json.dump(data, file, indent=4)
				act = "Removed an item."
				return act
			except IndexError:
				print("Invalid Index.\nReturn in 2 seconds.")
				time.sleep(2)
				return
	except ValueError:
		print("Arguments Required: Index.")
		input("Press any key to return.")
	return


def revert_data():
	try:	
		with open(backupdataname, "r") as backupfile:
			backup = json.load(backupfile)
			backupfile.close()
			data_backup()
			with open(dataname, "w") as file:
				json.dump(backup, file, indent=4)
				file.close()
			act = "Revert data to backup."
			return act
	except FileExistsError or FileNotFoundError:
		print("You don't have any auto created backup.")
		print("Backup will be created every time you edit the data in through this code.")
		input("Press any key to return.")
		return

# ------------------------ End of functions ----------------------------

# os.system("color 0c")
# os.system("title Interpreter")


while loop:
	if eocreach == max_eocreach-1:
		loop = False
	loaded_data = load_data()
	try:
		data, output, urloutput, recent_action = load_data()
	except ValueError:
		data, output, urloutput = load_data()
	os.system("cls")
	print(f"List:\n{output}")
	if output == "":
		print("Your List Is Empty, Consider Adding Something Here :(")
	if writeoutput:
		export_data(exportfolder)
	if recent_action == "":
		pass
	else:
		print(f"Recent Act: {recent_action}")
	print("Type exit to exit.\n[h]For help.")
	inpt = input(f"EOC:{eocreach}./>")
	try:
		inp = int(inpt)
		try:
			webbrowser.open(urloutput[inp])
			if exitafteropenurl:
				exit()
		except ValueError:
			print("Invalid index.")
			input("Press any key to return.")
	except ValueError:
		inp = str.lower(inpt)
		# Commands Without Argument Dependencies
		if inp == "export":
			recent_action = export_data(exportfolder)
			input("Press any key to return.")
		elif inp == "h" or inp == "help":
			helpmenu(inp)
			input("Press any key to return.")
		elif inp == "revert":
			recent_action = revert_data()

		# Commands With Argument Dependencies
		try:
			cmd = inp.split(" ")[0]
			if cmd == "h" or cmd == "help":
				helpmenu(inpt)
			elif cmd == "a" or cmd == "add" or cmd == "append":
				recent_action = add_data(inpt)
			elif cmd == "ins" or cmd == "insert":
				recent_action = insert_data(inpt)
			elif cmd == "rep" or cmd == "replace":
				recent_action = replace_data(inpt)
			elif cmd == "rmv" or cmd == "rem" or cmd == "remove" or cmd == "pop":
				recent_action = remove_data(inpt)
			elif cmd == "revert" or cmd == "rev" or cmd == "restore":
				recent_action = revert_data()
		except ValueError:
			print("Invalid Syntax")
			input("Press any key to return.")

		# Exit Command
		if inp == "exit":
			exit()

	eocreach += 1
	print("\n\n\n")
print(f"Woah! {max_eocreach} Loops? You are very dedicated!\nTime to stop though :)")
time.sleep(5)
