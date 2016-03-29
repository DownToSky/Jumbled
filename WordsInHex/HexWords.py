"""
1:I,l
2:z
5:S
A:A
B:B
C:C
D:D
E:E
F:F
"""

def ChangeToHex(word):
    word=word.lower()
    outPut=""
    for chr in word:
        if chr=='i' or chr=='l':
            outPut+="1"
            continue
        if chr=='z':
            outPut+="2"
            continue
        if chr=='s':
            outPut+="5"
            continue
        if chr=='a':
            outPut+="A"
            continue
        if chr=='b':
            outPut+="B"
            continue
        if chr=='c':
            outPut+="C"
            continue
        if chr=='d':
            outPut+="D"
            continue
        if chr=='e':
            outPut+="E"
            continue
        if chr=='f':
            outPut+="F"
            continue
        else:
            return None
    return outPut
    
def FindAllValidHexForm(fileName):
    with open(fileName+".txt","r") as dicFile:
        wordList= list(line.strip() for line in dicFile)
        hexWords=[]
        for word in wordList:
            hexForm = ChangeToHex(word)
            if not hexForm==None:
                hexWords.append([hexForm,word])
        with open(fileName+"Hex.txt","w") as hexFile:
            for i in range(0,len(hexWords)):
                hexFile.write(hexWords[i][0]+"::"+hexWords[i][1]+"\n")

FindAllValidHexForm("LangWords")
FindAllValidHexForm("PokemonNames")                   
