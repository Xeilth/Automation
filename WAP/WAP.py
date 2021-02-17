import json, webbrowser
url_table = {}
print(f'{"Keyword list":-^50}')
for item in json.load(open("Data.json", "r")):
    print(f'''{f"{'|'.join(item['keywords'])}":<20} --> {item['url']:>25}''')
    url_table.update({key: item['url'] for key in item['keywords']})
print(f"{'':-<50}")
while True:
    try:webbrowser.open_new(url_table[input("Keyword:")]) and exit()
    except KeyError: print("Invalid Key.")

# Original
"""
import webbrowser
import json

with open("Data.json", "r") as f:
    data = json.load(f)

url_referer = {}

print(f'{"Keyword list":-^50}')
for url_data in data:
    keywords = url_data['keywords']
    url = url_data['url']
    print(f'''{f"{'|'.join(keywords)}":<20} --> {url:>25}''')
    url_referer.update({key: url for key in keywords})


while True:
    key = input("Key:")
    try:
        webbrowser.open_new(url_referer[key])
        exit()
    except KeyError:
        print("Invalid Key.")
"""
