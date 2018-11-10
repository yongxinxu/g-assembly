from numpy import *
from genome_lib import *

'''
Part 1: Generating dot matrices - dot matrices allow biologists to visually compare two DNA sequences to determine alignment
'''
# this is a helpful function of dot_matrix()  
def equal_character(a, b, answer, index_a):
    assert (type(a)==type(b)==type("a string"))
    assert (len(a)==len(b) and len(a) > 0)
    
    n=len(a)
    
    if index_a >= n:
        return answer
    else:
        assert index_a < n
        
        for index_b in range(n): # to compare a[index_a] with each character of b
            if a[index_a] == b[index_b]:
                answer[index_a, index_b] = 1
                
        return equal_character(a, b, answer, index_a + 1) # move to next character of a    
    # postcondition: the entry at (index_a)th row and (index_b)th column change to 1 when a[index_a] == b[index_b].

# dot_matrix() takes two DNA sequences and returns their dot matrix
def dot_matrix(seq_a, seq_b):
    assert (type(seq_a)==type(seq_b)==type("a string")) # sequences are strings
    assert len(seq_a)==len(seq_b) # the lengths of two sequences should be equal and greater than zero
    
    n = len(seq_a)
    answer = zeros([n,n], dtype=int) # create a two-dimensional array with all zeros 
    
    return equal_character(seq_a, seq_b, answer, 0)
    # postconditon: the result is the square matrix of the two sequences, in which the entry in the ith row and jth coloumn
    #               should be 0 if the ith character of the first sequence is not equal to the jth character of the second
    #               sequence and be 1 if these characters are equal. 


       
'''
Part 2: Converting from DNA sequences to amino acid abbreviation
'''
def dna_aa(dna, index, mydictionary):
    assert (isinstance(dna, str) and isinstance(index, int) and isinstance(mydictionary, dict))
    assert (len(dna) % 3 == 0) 
    
    if index == len(dna):
        return mydictionary
    else:
        converted_amino_acid = get_amino_acids_dict()[dna[index:index+3]] # convert the first three dna into an amino acid
        
        if converted_amino_acid not in mydictionary: # if this amino acid is the first time to appear
            mydictionary [converted_amino_acid] = 1
        else: 
            assert converted_amino_acid in mydictionary
            count_so_far = mydictionary[converted_amino_acid]
            mydictionary[converted_amino_acid]=count_so_far + 1 # the times that amino acid was found was added by 1
        return dna_aa(dna, index+3, mydictionary)
    # postcondition: the result  maps from amino acid abbreviation to the count of the numbers of times that amino
    #                acid was found in the sequence.
    
def amino_acids(dna):
    assert (isinstance(dna, str))
    assert (len(dna) % 3 == 0) # to make sure all DNA can be converted into amino acids.
    
    return dna_aa(dna, 0, {})
    # postcondition: the output maps from amino acid abbreviation to the count of the numbers of times that amino
    #                acid was found in the sequence.


'''
Part 3: Merging DNA fragments together into a single sequence that most causes the fragments to overlap
'''

def count_overlap(fragment1, fragment2): 
    # this function is based on dox_matrix function, traceing the diagonal pattern of 1 and count the number of 1 on the diagonal which
    # starts from the fisrt column and ends at the last row
    
    assert (isinstance(fragment1, str) and isinstance(fragment2, str))
    
    matrix = dot_matrix(fragment1, fragment2) # form the dot matrix of two fragments
    
    for row in range(len(matrix)): # to check vertically
        
        count = 0 
        
        for column in range(len(matrix[0])+1): # to check diagonally
            if row == len(matrix): # if variable row gets to the last row, return the count of 1
                return count
            elif matrix[row, column] == 1: # when the element is 1, continue going diagonally
                count = count + 1
                row = row + 1
            else: # when the element is 0, exit this loop and go back to check vertically
                break
        
    return count
    # postcondition: the result is the count of the overlapping letters in two fragments when fragment 1 is in front of fragment 2
    

def select_fragment(sofar, rest, length):
    assert (isinstance(sofar, str) and isinstance(rest, list) and isinstance(length, int))
    index = 0
    record_index = 0
    biggest_count = 0
    
    while index < len(rest):       
        count = count_overlap(sofar[-length:], rest[index]) # sofar[-length:] is to make sure the length of the sequences are the same     
        if count > biggest_count: 
            biggest_count = count
            record_index = index
        index = index + 1
    return rest[record_index]
    # postcondition: the answer is the fragment from the list having the most letters overlap with the sofar


def put_fragments_together(fragments):
    assert (isinstance(fragments, list))
    
    if len(fragments) == 0: # if fragments is an empty list, return empty string
        return ""
    
    sofar = fragments[0]
    rest = fragments[1:]
    n = len(sofar)
    while len(rest) > 0:
        next_fragment = select_fragment(sofar, rest, n) # the fragment having the most overlap
        number = count_overlap(sofar[-n:], next_fragment) # get the index of the overlap part
        sofar = sofar + next_fragment[number:] 
        rest.remove(next_fragment) # remove this fragment from the list
    return sofar
    # postcondition: the answer is the shortest possible resulting sequence by overlapping the all the fragments.
 
