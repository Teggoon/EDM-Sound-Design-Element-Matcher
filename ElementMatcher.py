import json
import random


with open('elements.json', 'r') as file:
    fileRead = file.read().replace('\n', '')


#Read JSON data file
data = json.loads(fileRead)

#number of categories for match-making
categoryNum = len(data["entries"])

#Object containing sub-branches
exceptions = data["exceptions"]

#Writer to file
savedFileWriter = open("saved_matches.txt","a+");

#List storing current match
currentMatch = []

userInput = ""

#Continue to run while the user wants it
while userInput != "q":

    #for each category
    for i in range(0, categoryNum):

        wentIn = False
        entryNum = len(data["entries"][i]["elems"])
        picker = random.randint(0,entryNum - 1)
        pickedElement = data["entries"][i]["elems"][picker]

        #looping through the keys in the exception list
        for key in exceptions.keys():

            #if found picked element needing stepping in
            if key == pickedElement:
                wentIn = True
                entryNum = len(data["exceptions"][key])
                picker = random.randint(0,entryNum - 1)
                outputString = "--- " + key + " - " + data["exceptions"][key][picker];


                print(outputString);
                currentMatch.append(outputString);
                break;

        if wentIn == False:
            outputString = "--- " + pickedElement;
            print(outputString);
            currentMatch.append(outputString);


    print("\nA match has been generated. Press s to save current match, enter to continue, q to quit");


    userInput = input();
    if userInput == " ":
        currentMatch = []
        continue
    elif userInput == "s":
        output = "------------------------------------------------------\n\n"
        output += " \n".join(currentMatch)
        output += "\n\n"
        savedFileWriter.write(output)
        currentMatch = []
        output = ""
    elif userInput == "q":
        print("Exiting program.");

savedFileWriter.close();
