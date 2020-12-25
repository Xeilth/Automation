import webbrowser
import json


# New Default Array Configuration

defaultarray = []
url_names = []

with open("Data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

for urlinfo in data["urlinfo"]:
    url = urlinfo["url"]
    letter1 = urlinfo["letter1"]
    letter2 = urlinfo["letter2"]
    nickname = urlinfo["name"]
    defaultarray.extend([url, letter1, letter2])
    url_names.extend([nickname])

# Set Default Url (0, 3, 6, 9....)
# Default Url Set Accordingly With Your Array Size, Each Url is Expected to Take 3 Indexed Space on The Array.
#defaultindex = 0
defaultindex = data['defaultindex']
default = defaultarray[defaultindex]

# End of Default Array Configuration

# Default Array Debug
'''
#print(urlamount)
#print(defaultarray)
#print(len(defaultarray))
#print(defaultarray[3])
#print(default)
'''


# Seperator Inputing
seperator_chars = []
for seperator in data["seperator"]:
    seperator_chars.extend(seperator)

# Seperator Debug
#print(seperator_chars)


# Start of Functions

def websearch():
    print("Default Url " + url_names[int(defaultindex/3)] + " | " + str(default))
    deflen = len(defaultarray)
    deflen2 = int(deflen/3)

    def parameterdefine():
        print("There Are " + str(deflen2) + " Listed Url")
        for i in range(deflen2):
            if i <= deflen2:
                print(str(i) + " For " + url_names[i] + " | "+ defaultarray[i*3])
        del i
        return deflen2

    parameterdefine()

    inpt = input("Url Parameter : ")

    # Dual Input Problem :))
    i = 1
    exceptions = 0
    while i <= len(seperator_chars):
        try:
            urlset, text = inpt.split(seperator_chars[i-1], 1)
        except ValueError:
            exceptions += 1
        i += 1
    try:
        urlset
    except NameError:
        urlset = inpt
    del i


    # Debug line (Dual Input)
    #print(urlset)
    #print(exceptions)
    '''
    if exceptions == deflen2 + 1:
       print("Bad Dual Input")
    elif exceptions == deflen2:
       print("Dual Input Is Doing Great!")
    else:
       print("Something is Very Very Wrong In Dual Input :(")
    print("exceptions:" + exceptions)
    '''
    #print(text)


    def checkparameter():
        global deflen3a
        i = 1
        while i <= deflen2:
            if urlset == str(i - 1):
                deflen3a = (3 * i) - 1
                i += 1
            else:
                i += 1
        try:
            deflen3a
        except NameError:
            deflen3a = defaultindex + 2
            print("\nInvalid Url, Using Default Url (" + default + ").\n")
        del i
        return deflen3a

    deflen3 = checkparameter()

    # Debug Line
    #print(deflen3)

    url = defaultarray[int(deflen3 - 2)]
    letter1 = defaultarray[int(deflen3 - 1)]
    letter2 = defaultarray[int(deflen3)]

    try:
        text
    except NameError:
        text = input("Search : ")

    result = ""
    for letter in text:
        if letter == letter1:
            result += letter2
        else:
            result += letter
    link = url + result
    webbrowser.open_new_tab(link)
    print("Visiting " + link)
    return link

# End of Functions



# Executors


#websearch()
webbrowser.Chrome(websearch())
#webbrowser.Mozilla(websearch())
#webbrowser.WindowsDefault(websearch())
#webbrowser.open(websearch())
