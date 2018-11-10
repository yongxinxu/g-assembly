"""
A library for dealing with genomes, including for parsing fasta input.
"""


def get_amino_acids_dict():
    """
    Returns a dictionary that maps from three-character (lower case) dna strings to
    single character (upper case) amino acid codes.  Stop is represented by
    "Z". The first "atg" in a sequence is the start codon.  See wikipedia for a full chart:
    http://en.wikipedia.org/wiki/DNA_codon_table
    
    >>> get_amino_acids_dict()['ccc']
    'P'
    
    """
    codon_table = {'ttt' : 'F', 'ttc' : 'F',
            'tta' : 'L', 'ttg' : 'L', 'ctt' : 'L', 'ctc' : 'L', 'cta' : 'L', 'ctg' : 'L',
            'att' : 'I', 'atc' : 'I', 'ata' : 'I',
            'atg' : 'M',
            'gtt' : 'V', 'gtc' : 'V', 'gta' : 'V', 'gtg' : 'V',
            'tct' : 'S', 'tcc' : 'S', 'tca' : 'S', 'tcg' : 'S',
            'cct' : 'P', 'ccc' : 'P', 'cca' : 'P', 'ccg' : 'P',
            'act' : 'T', 'acc' : 'T', 'aca' : 'T', 'acg' : 'T',
            'gct' : 'A', 'gcc' : 'A', 'gca' : 'A', 'gcg' : 'A',
            'tat' : 'Y', 'tac' : 'Y',
            'taa' : 'Z', 'tag' : 'Z',
            'cat' : 'H', 'cac' : 'H',
            'caa' : 'Q', 'cag' : 'Q',
            'aat' : 'N', 'aac' : 'N',
            'aaa' : 'K', 'aag' : 'K',
            'gat' : 'D', 'gac' : 'D',
            'gaa' : 'E', 'gag' : 'E',
            'tgt' : 'C', 'tgc' : 'C',
            'tga' : 'Z',
            'tgg' : 'W',
            'cgt' : 'R', 'cgc' : 'R', 'cga' : 'R', 'cgg' : 'R',
            'agt' : 'S', 'agc' : 'S',
            'aga' : 'R', 'agg' : 'R',
            'ggt' : 'G', 'ggc' : 'G', 'gga' : 'G', 'ggg' : 'G'
            }
    return codon_table


def get_test_fragments():
    """
    Returns a small list of testing fragments.
    
    >>> len(get_test_fragments())
    5
    
    """
    return ['tttttt', 'ttttgg', 'tggaga', 'agacgc', 'cgcggg']


def get_fragments():
    """
    Gets the fasta input from input.fasta, parses it, and returns a list of fragments. For more on the 
    FASTA format see: http://en.wikipedia.org/wiki/FASTA_format

    This is also the input that should be used for the extra credit, though you may actually find that
    you're able to match fewer fragments once you consider the complement.

    >>> len(get_fragments())
    295
    """
    return parse("input.fasta")

def get_orig_fragments():
    """
    Returns the full original fasta input file.  Only call this function if you're done with everything and
    are up for a real challenge.
    
    >>> len(get_orig_fragments())
    300
    
    """
    return parse("input_orig.fasta")

def parse(filename):
    """
    Gets the input from the given fasta file and parses it to return a list of fragments.
    """
    f = open(filename, 'r')
    fragments = []
    frag_str = ""
    for line in f:
        if ">" in line:
            if frag_str != "":
                fragments.append(frag_str)
            frag_str = ""
        else:
            frag_str += line.strip()
    fragments.append(frag_str)
    return fragments

# make doctest work:
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
