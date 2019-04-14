import textwrap

from helpers import clean_string, create_list_of_strings


def mutation_gui():
    '''
    Takes user input and runs the specified program
    '''

    choice = 1
    while choice != 2:
        print(
            textwrap.dedent(
                """
                Welcome to the Mutation Detector!

                Please choose from the following options:
                0) Format Genetic Information from 'GeneDataBase.txt'
                1) Run MutD
                2) Exit Program
                """
            )
        )

        choice1 = int(input("Make your choice here: "))
        if choice1 == 0:
            format_page()
        if choice1 == 1:
            mutation_d()

        return


def sequence_gene_filter(list_from_file):
    '''
    Filters the gene sequence
    '''

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

    with open("FormattedDatabase.txt", "w") as _file:
        _file.write(gene_string)

    mutation_gui()


def mutation_d():
    with open("GeneDatabase.txt") as gene_ref:
        master_list = [line.replace('\n', '') for line in gene_ref]

    gene_acronym, just_gene_seq = sequence_gene_filter(master_list)

    gene_dict = {}
    for index, _ in enumerate(gene_acronym):
        gene_dict[gene_acronym[index]] = just_gene_seq[index]

    print('gene_dict', gene_dict)

    print("Welcome to the Mutation Detector")
    print("Currently the Database consists of the following Genes: ")

    for index, _ in enumerate(gene_acronym):
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

    mutation_gui()


if __name__ == "__main__":
    mutation_gui()
