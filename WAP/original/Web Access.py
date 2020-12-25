import webbrowser
import json

with open("Data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

keywordlist = {
    "yt": "youtube",
    "mal": "myanimelist",
    "tk": "tokopedia",
}
codelist = {
    0: "google",
    1: "youtube",
    2: "osu",
    3: "myanimelist"
}

names = {
    "default": "https://www.google.com",
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "osu": "https://osu.ppy.sh",
    "myanimelist": "https://myanimelist.net/search/all?q=",

    "amazon": "https://www.amazon.com",
    "tokopedia": "https://www.tokopedia.com"
}

def urlconvert():
    nameinput = str.lower(input("Site Name : "))
    key = keywordlist.get(nameinput, nameinput)
    if key == nameinput:
        code = codelist.get(nameinput, nameinput)
        url = names.get(code, names.get("default"))
    else:
        url = names.get(key, names.get("default"))
    print("Visiting " + url)
    webbrowser.open_new_tab(url)


urlconvert()
#webbrowser.Chrome(urlconvert())
