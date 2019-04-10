def formatPage():
    with open("GeneDatabase.txt") as geneRef:
        masterList = [line for line in geneRef]
    output = open("FormattedDatabase.txt", "w")
    lastList =[]
    y = 0
    for x in masterList:
        lastList.append(masterList[y].rstrip('\n'))
        y += 1
    realList = []
    for x in lastList:
        for z in x:
            realList.append(z)
    anotherList = []
    for x in realList:
        if x.isalpha():
            anotherList.append(x)
    print(anotherList)
    y = 0
    strList = ''
    for x in anotherList:
        strList += x
    output.write(strList)
    output.close()
    geneRef.close()
    
