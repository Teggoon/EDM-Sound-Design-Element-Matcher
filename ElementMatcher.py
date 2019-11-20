import json
import random

with open('elements.json', 'r') as file:
    fileRead = file.read().replace('\n', '')


data = json.loads(fileRead)

categoryNum = len(data["entries"])

print("Number of categories: " + str(categoryNum))

exceptions = data["exceptions"]


for i in range(0, categoryNum):

    wentIn = 0
    entryNum = len(data["entries"][i]["elems"])
    picker = random.randint(0,entryNum - 1)

    for key in exceptions.keys():

        if key == data["entries"][i]["elems"][picker]:
            wentIn = 1
            entryNum = len(data["exceptions"][key])
            picker = random.randint(0,entryNum - 1)
            print(data["entries"][i]["name"] + ": " + key + " - " + data["exceptions"][key][picker]);
            break;

    if wentIn == 0:
        print(data["entries"][i]["name"] + ": " + data["entries"][i]["elems"][picker]);
