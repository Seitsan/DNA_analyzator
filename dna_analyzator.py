def dna_analyzator(dna:str):
    """
    Takes DNA sequence as input and counts a quantity of a nucleotides, G- and C-nucleotides,
    GC content percentage accurate to two decimal places
    :param dna: A DNA sequence as string
    :return: The strings with information about quantity of a nucleotides, G- and C-nucleotides
    quantity, GC percentage accurate to two decimal places
    """
    nucleotides_quantity = len(dna)
    g_quantity = dna.count('g')
    c_quantity = dna.count('c')
    gc_content = round((g_quantity + c_quantity) / nucleotides_quantity * 100, 2)
    print(f'Nucleotides quantity: {nucleotides_quantity}')
    print(f'G quantity: {g_quantity}')
    print(f'C quantity: {c_quantity}')
    print(f'GC content: {gc_content}%')


def dna_verification(dna:str) -> bool:
    """
    Takes DNA sequence as input and check if all characters are nucleotides
    :param dna: A DNA sequence as string
    :return: True or False
    """
    return set(dna).issubset({'a', 't', 'g', 'c'})


def main():
    sequence = input('Input a DNA sequence: ')
    dna = sequence.lower()
    if dna_verification(dna):
        dna_analyzator(dna)
    else:
        print('This string is not a DNA sequence')

main()