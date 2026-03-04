#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    x = open(fileName)
    longest_text = x.readline()
    longest = len(longest_text)
    for line in x:
        z = len(line)
        if z > longest:
            longest_text = line
            longest= z
        else:
            continue
    return(longest_text)





def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    theFile = open(fileName)
    Answer = [""]
    insertPlace = 0
    allStuff = theFile.readline()
    while len(allStuff) > 1:
        Answer.insert(insertPlace, allStuff[0:8])
        insertPlace += 1
        allStuff = allStuff[8:]
    realAnswer = Answer.pop(-1)
    return(Answer)
