def MutD():
    with open("GeneticDatabase.txt") as geneRef:
        masterList = [line for line in geneRef]
    lastList =[]
    y = 0
    for x in masterList:
        lastList.append(masterList[y].rstrip('\n'))
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
    geneDict = {}
    x = 0
    for element in geneAcronym:
        geneDict[geneAcronym[x]] = finalSequence[x]
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


