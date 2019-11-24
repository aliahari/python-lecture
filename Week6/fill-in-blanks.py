numBlanks = 0
golden = ["Emptiness", "fear", "mountain"]
newLines = []
with open('fill-blanks.txt', 'r') as f:
    for line in f:
        if '...' in line:
            blank = input("Fill the blank in " + line)
            if blank == golden[numBlanks]:
                newLine = line.replace("...", blank)
            else:
                newLine = line
            numBlanks += 1
        else:
            newLine = line
        newLines.append(newLine)
print(newLines)

