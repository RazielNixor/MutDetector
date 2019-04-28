def MutationDetector():
    geneRef = open("GeneticDatabase.txt")
    geneSequence = [geneRef.readline()]
    geneAcronym = [geneRef.readline()]
    x = 0
    while x < len(geneAcronym):
        geneDict = {}
        geneDict[geneAcronym[x]] = geneSequence[x]
        x += 1
    for nucleotide in geneDict.values():
        geneValues = []
        geneValues.append(nucleotide)
    print("Welcome to the Mutation Detector")
    print("Currently the Database consists of the following Genes: ")

    x = 0
    for genes in geneAcronym:
        print("{}) Gene: ".format(x), geneAcronym[x])
        x += 1
    print("The sequence being tested must be as long as the gene sequence being tested against")
    gene = geneValues[int(input("Please Select Your Gene of Interest: "))]
    geneList = [nucleotide for nucleotide in gene]
    geneTest = input("Please Input the Sequence you wish to test: ")
    nucleotideList = [nucleotide for nucleotide in geneTest]
    x = 0
    while x < len(geneList):
        if geneList[x] == '\n':
            geneList.pop()
        x += 1
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
