def MutGUI():
    choice = 1
    while choice != 2:
        print()
        print("Welcome to the Mutation Detector!")
        print()
        print()
        print("Please choose from the following options:")
        print("0) Format Genetic Information from 'GeneDataBase.txt'")
        print("1) Run MutD")
        print()
        print("2) Exit Program")
        print()
        choice1 = int(input("Make your choice here: "))
        if choice1 == 0:
            formatPage()
        if choice1 == 1:
            MutD()
        return

def sequenceGeneFilter(list_from_file):
    lastList =[]
    y = 0
    for x in list_from_file:
        lastList.append(list_from_file[y].rstrip('\n'))
        y += 1
    geneAcronym = []
    geneSequence = []
    finalSequence = []
    geneSeq = ''
    for x in lastList:
        z = len(x)
        refresh = False
        if z < 10:
            refresh = True
            geneAcronym.append(x)
        if z >= 10:
            geneSequence.append(x)
            for y in x:
                geneSeq += str(y)
        if refresh == True:
            finalSequence.append(geneSeq)
            geneSequence.clear()
            geneSeq = ''
    y = 0
    strSeq = ''
    lastList = []
    justGeneSeq = []
    for x in geneSequence:
        for z in x:
            if z.isalpha():
                lastList.append(z)
                strSeq += z
    justGeneSeq.append(strSeq)
    return geneAcronym, finalSequence, justGeneSeq

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
    y = 0
    strList = ''
    for x in anotherList:
        strList += x
    output.write(strList)
    output.close()
    geneRef.close()
    print(strList)
    return MutGUI()

def MutD():
    with open("GeneDatabase.txt") as geneRef:
        masterList = [line for line in geneRef]
    geneAcronym, finalSequence, justGeneSeq = sequenceGeneFilter(masterList)
    x = 0
    geneDict = {}
    for element in geneAcronym:
        geneDict[geneAcronym[x]] = justGeneSeq[x]
        x += 1

    print("Welcome to the Mutation Detector")
    print("Currently the Database consists of the following Genes: ")
    
    x = 0
    for genes in geneAcronym:
        print("{}) Gene: ".format(x), geneAcronym[x])
        x += 1
    print("The sequence being tested must be as long as the gene sequence being tested against")
    gene = geneAcronym[int(input("Please Select Your Gene of Interest: "))]
    geneList = [nucleotide for nucleotide in geneDict[gene]]
    geneTest = input("Please Input the Sequence you wish to test: ")
    nucleotideList = [nucleotide for nucleotide in geneTest]
    # Index Error due to discrepancy between length of geneList and nucleotideList
    # Fixed by removing space caused by line break from copy and paste
    y = 0
    mutationIndex = []
    for x in nucleotideList:
        if x != geneList[y]:
            mutationIndex.append(y)
            y += 1
        else:
            y += 1
    print("Gene Mutations found at positions ", mutationIndex)
    G = [geneList[x] for x in mutationIndex]
    N = [nucleotideList[x] for x in mutationIndex]
    print("Nucleotides {} were mutated to {}".format(G, N))
    print("Total Mutations found: ", len(mutationIndex))
    geneRef.close()
    return MutGUI()

