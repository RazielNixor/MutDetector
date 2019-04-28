import textwrap


from helpers import clean_string, create_list_of_strings


def mutation_gui():
    choice1 = 1
    while choice1 != 3:
        print(
            textwrap.dedent(
                '''
        Welcome to the Mutation Detector!


        Please choose from the following options:
        0) Format Genetic Information from 'GeneDataBase.txt'
        1) Run mutation_detector
        2) Run amino_acid_detector

        3) Exit Program"
        '''
            )
        )
        choice1 = int(input("Make your choice here: "))
        if choice1 == 0:
            format_page()
        if choice1 == 1:
            mutation_detector()
        if choice1 == 2:
            mutation_detector()
            codon_summary()
        return


def sequence_gene_filter(list_from_file):
    gene_acronym = []
    gene_sequence = []
    gene_seq = ''
    for line in list_from_file:
        line_length = len(line)
        refresh = False
        if line_length < 10:
            refresh = True
            gene_acronym.append(line)
        else:
            gene_sequence.append(line)
            gene_seq += line
        if refresh:
            gene_sequence.clear()
            gene_seq = ''

    str_seq = ''
    just_gene_seq = []
    for line in gene_sequence:
        str_seq += clean_string(line)

    just_gene_seq.append(str_seq)
    return gene_acronym, just_gene_seq


def format_page():
    with open("GeneDatabase.txt") as _file:
        data = _file.read().replace('\n', '')

    gene_string = clean_string(data)

    with open("formattedDatabase.txt", "w") as _file:
        _file.write(gene_string)

    gene_string = gene_string.upper()
    print(gene_string)
    mutation_gui()


def mutation_detector():
    with open("GeneDatabase.txt") as gene_ref:
        master_list = [line for line in gene_ref]

    gene_acronym, just_gene_seq = sequence_gene_filter(master_list)

    gene_dict = {}
    for index, _ in enumerate(gene_acronym):
        gene_dict[gene_acronym[index]] = just_gene_seq[index]

    print("Welcome to the Mutation Detector")
    print("Currently the Database consists of the following Genes: ")

    for index, x in enumerate(gene_acronym):
        print("{}) Gene: ".format(index), gene_acronym[index])

    print("The sequence being tested must be as long as the gene sequence being tested against")
    gene = gene_acronym[int(input("Please Select Your Gene of Interest: "))]
    gene_list = [nucleotide for nucleotide in gene_dict[gene]]
    gene_test = input("Please Input the Sequence you wish to test: ")
    nucleotide_list = [nucleotide for nucleotide in gene_test]
    # Index Error due to discrepancy between length of gene_list and nucleotide_list
    # Fixed by removing space caused by line break from copy and paste

    length_difference = len(gene_list) - len(nucleotide_list)
    nucleotide_list.extend(create_list_of_strings('', length_difference))

    mutation_index = [index for index, val in enumerate(gene_list) if val != nucleotide_list[index]]

    print("Gene Mutations found at positions ", mutation_index)
    genes = [gene_list[val] for val in mutation_index]
    nucleotides = [nucleotide_list[val] for val in mutation_index]
    print("Nucleotides {} were mutated to {}".format(genes, nucleotides))
    print("Total Mutations found: ", len(mutation_index))

    protein_file = open("strings_for_proteins.txt", "w")
    nucleotide_str = str(''.join(nucleotide_list))
    gene_str = str(''.join(gene_list))
    protein_file.write(nucleotide_str + '\n')
    protein_file.write(gene_str + '\n')
    protein_file.close()

    return nucleotide_str, gene_str


CODONS = {
    'TTT': 'Phe',
    'TTC': 'Phe',
    'TTA': 'Leu',
    'TTG': 'Leu',
    'CTT': 'Leu',
    'CTC': 'Leu',
    'CTA': 'Leu',
    'CTG': 'Leu',
    'ATT': 'Ile',
    'ATC': 'Ile',
    'ATA': 'Ile',
    'ATG': 'Met',
    'GTT': 'Val',
    'GTC': 'Val',
    'GTA': 'Val',
    'GTG': 'Val',
    'TCT': 'Ser',
    'TCC': 'Ser',
    'TCA': 'Ser',
    'TCG': 'Ser',
    'CCT': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',
    'ACT': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',
    'GCT': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',
    'TAT': 'Tyr',
    'TAC': 'Tyr',
    'TAA': 'Stop',
    'TAG': 'Stop',
    'CAT': 'His',
    'CAC': 'His',
    'CAA': 'Gln',
    'CAG': 'Gln',
    'AAT': 'Asn',
    'AAC': 'Asn',
    'AAA': 'Lys',
    'AAG': 'Lys',
    'GAT': 'Asp',
    'GAC': 'Asp',
    'GAA': 'Glu',
    'GAG': 'Glu',
    'TGT': 'Cys',
    'TGC': 'Cys',
    'TGA': 'Stop',
    'TGG': 'Trp',
    'CGT': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGT': 'Ser',
    'AGC': 'Ser',
    'AGA': 'Arg',
    'AGG': 'Arg',
    'GGT': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
    'AA': 'Stop',
    'AT': 'Stop',
    'AC': 'Stop',
    'AG': 'Stop',
    'TT': 'Stop',
    'TA': 'Stop',
    'TC': 'Stop',
    'TG': 'Stop',
    'CC': 'Stop',
    'CA': 'Stop',
    'CT': 'Stop',
    'CG': 'Stop',
    'GG': 'Stop',
    'GA': 'Stop',
    'GT': 'Stop',
    'GC': 'Stop',
}


def codon_change(list_of_sequence_nucleotides):
    #    Regex solution to the problem
    #    codon_sequence = re.findall('...',list_of_sequence_nucleotides)
    n = 3
    codon_sequence = [list_of_sequence_nucleotides[i : i + n] for i in range(0, len(list_of_sequence_nucleotides), n)]
    caps_sequence = [codon.upper() for codon in codon_sequence]
    return caps_sequence


gene_list = []
nucleotide_list = []


def codon_summary():
    protein_file = open("strings_for_proteins.txt", "r")
    nucleotide_str = protein_file.readline()
    gene_str = protein_file.readline()
    protein_file.close()
    nucleotide_str = nucleotide_str.replace('\n', '')
    gene_str = gene_str.replace('\n', '')

    gene_str = gene_str.upper()
    nucleotide_str = nucleotide_str.upper()

    codon_genes = codon_change(gene_str)
    codon_nucleotides = codon_change(nucleotide_str)
    caps_genes = [codon.upper() for codon in codon_genes]

    codon_mutation_index = [index for index, codon in enumerate(codon_genes) if codon_nucleotides[index] != codon]

    amino_acid_mutants = []
    amino_acid_reference = []
    codon_mutant_nucleotides = []
    codon_mutant_gene = []
    for index in codon_mutation_index:
        amino_acid_mutants.append(CODONS[codon_nucleotides[index]])
        amino_acid_reference.append(CODONS[caps_genes[index]])
        codon_mutant_nucleotides.append(codon_nucleotides[index])
        codon_mutant_gene.append(caps_genes[index])
        try:
            index = "TAG"
        except KeyError:
            print("The sequence you entered is shorter than it should be")
    print("Amino Acids {} were mutated to {}".format(amino_acid_reference, amino_acid_mutants))
    print("Codons {} were mutated to {}".format(codon_mutant_gene, codon_mutant_nucleotides))
    print("Total Mutation in the Protein: ", len(codon_mutation_index))


mutation_gui()

if __name__ == "__main___":
    mutation_gui()
