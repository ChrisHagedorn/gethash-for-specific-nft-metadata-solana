# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
from urllib.request import urlopen, Request



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    print_hi('chris')
    print('[')

    file1 = open("message.txt", "r")
    # f = open("gib-meta.json", "r")
    hashlist = []
    newhash= []
    # data = json.load(file2)
    count = 0
    count2 = 0

    for lines in file1:
        hashlist.append(lines.strip()[1:-2])

    with open('gib-meta.json', 'r') as s:
        result = json.load(s)

    for data in result:
        url = data["tokenData"]["uri"]
        r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(r)
        uri_data = json.loads(response.read())
        if (uri_data["attributes"][2]["value"] == "Earth"):
            print(f'"{data["mint"]}",')
            count2 = count2 + 1

        # for metadata in uri_data:
        #     print(metadata[2])
        #     count2 = count2 + 1

        # attributes = data['metadata']['attributes']
        # print(attributes[2])
        # mint_address = [data['mint'] for traits in attributes if traits['trait_type'] == "Elements"]
        # print(f'"{mint_address[0]}",')
        count = count + 1
            # newhash.append(element["mint"s])
    print(']')
    print(count)
    print(count2)
    # parameter for urlopen

    # store the response of URL

    # storing the JSON response
    # from url in data

main();