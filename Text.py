import json

class TextFile():
    def newTextFile(fileName, fileAddress):
        fileString = '.txt'
        if(fileAddress == None):    
            fileString = fileName + fileString
        else:
            fileString = fileAddress + '/' + fileName + fileString
        try:
            with open(fileString, 'w') as f:
                f.write('Created a new text file.')
                f.close()
        except FileNotFoundError:
            print("The " + fileAddress + " directory does not exist.")

    def getLocalAddress(fileName):
        return fileName + '.txt'

    def writeTextFile(fileAddress, str):
        try:
            with open(fileAddress, 'w') as f:
                f.write(str)
                f.close()
        except FileNotFoundError:
            print("The " + fileAddress + " text file does not exist.")

    def readTextFile(fileAddress):
        f = open(fileAddress, 'r')
        str = f.read()
        return str

    def textToJSON(fileAddress, fields):
        dict1 = {}
        try:
            with open(fileAddress) as f:
                num = 1
            for str in f:
                description = list(str.strip().split(None, len(fields)))
                item = 'dictItem' + str(num)
                i = 0
                dict2 = {}
                while i < len(fields):
                    dict2[fields[i]]= description[i]
                    i = i + 1
                dict1[item]= dict2
                l = l + 1
            JSONfile = open("test2.json", "w")
            json.dump(dict1, JSONfile, indent = 4)
            JSONfile.close()
        except FileNotFoundError:
            print("The " + fileAddress + " JSON file does not exist.")
        
    ## def JSONToText(fileAddress): for later

class FillText():
    def setRepeatedString(str, strLength, length):
        if len(str) > strLength:
            print("String length is too long, please make it shorter.")
        else:
            numTimes = int(strLength / len(str))
            newStr = ((str * numTimes) + '\n')* length
            return newStr