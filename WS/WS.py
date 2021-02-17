import webbrowser
import json

with open("Data.json", "r") as f:
    data = json.load(f)

url_referer = {}

print(f'{"Keyword list":-^45}')
for url_data in data:
    keywords = url_data['keywords']
    url = url_data['url']
    print(f'''{f"{'|'.join(keywords)}":<20} --> {url.split("/")[2]:>20}''')
    url_referer.update({key: url for key in keywords})

print(f"{'':-<45}\nSyntax: <Keyword> <Query>")
while True:
    try:
        SE, query = input("Input:").split()
        webbrowser.open_new(f"{url_referer[SE]}{query}")
        exit()
    except ValueError:print("Invalid Syntax.")
    except KeyError:print("Invalid Search Engine.")
