import webbrowser
import json

with open("Data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

keywordlist = data["keywordlist"]
codelist = data["codelist"]
namelist = data["namelist"]

try:
    defaultname = data["defaultname"]
    namelist["default"] = namelist.get(defaultname, "https://www.google.com")
except TypeError:
    print("Invalid Defaultname in json, defaultname doesn't exist in namelist.\nUsing Absolute Default.")
except KeyError:
    print("Default Name Value Isn't Detected In json.\nUsing Absolute Default.")

'''
# Displaying Dictionary
print(keywordlist)
keylistsname = ["Keyword List", "Code List"]
keylists = [keywordlist, codelist]
a = 0
while a <= 1:
    print(keylistsname[a])
    for i in keylists[a]:
        print(i + " As " + keylists[a][i])
    print("")
    a += 1

print("Name List")
for i in namelist:
    print(i + " As " + namelist[i])
'''

def urlconvert():
    nameinput = str.lower(input("Key : "))
    key = keywordlist.get(nameinput, nameinput)
    if key == nameinput:
        key = codelist.get(key, key)
    url = namelist.get(key, "Invalid")
    if url == "Invalid":
        url = namelist.get("default")
        print("invalid Name, Visiting Default Site " + url)
    print("Visiting " + url)
    webbrowser.open_new_tab(url)


urlconvert()
#webbrowser.Chrome(urlconvert())
