import webbrowser
#Guide
#add 'defaultarray.extend(["Url + Parameter Placeholder", "Input to Change(Ex:Space)", "Change Input to...(Ex: +, %20)"])'

defaultarray = []
defaultarray.extend(["https://www.youtube.com/results?search_query=", " ", "+"])
defaultarray.extend(["https://osu.ppy.sh/beatmapsets?q=", " ", "%20"])

#Set Default Url (0, 3, 6, 9....)
#Default Url Set Accordingly With Your Array Size, Each Url is Expected to Take 3 Indexed Space on The Array.
default = defaultarray[0]

def webchange():
    print("Default Url " + str(default))
    deflen = len(defaultarray)
    deflen2 = deflen/3
    deflen2 = int(deflen2)

    def parameterdefine():
        global urlset
        print("There Are " + str(deflen2) + " Url Parameter")
        for i in range(deflen2):
            if i < deflen2:
                print(str(i) + " For " + defaultarray[i*3])
                i += 1
            else:
                print(str(i) + " For " + defaultarray[i*3])
        return deflen2

    parameterdefine()
    urlset = input("Url Parameter : ")
    def checkparameter():
        global deflen3a
        for i in range(deflen2):
            if i <= deflen2:
                var = urlset == str(i - 1)
                deflen3a = deflen2 * i - 1
            else:
                deflen3a = deflen2 - 1
                print("")
                print("Invalid Input, Using Default Url (" + defaultarray[0] + ").")
                print("")
        return deflen3a

    deflen3 = checkparameter()
    url = defaultarray[int(deflen3 - 2)]
    letter1 = defaultarray[int(deflen3 - 1)]
    letter2 = defaultarray[int(deflen3)]

    text = input("Search : ")
    result = ""
    for letter in text:
        if letter == letter1:
            result += letter2
        else:
            result += letter
    link = url + result
    webbrowser.open(link)
    print("Visiting " + link)
    return link


#webchange()
webbrowser.Chrome(webchange())
#webbrowser.Mozilla(webchange())
#webbrowser.WindowsDefault(webchange())
#webbrowser.open(webchange())