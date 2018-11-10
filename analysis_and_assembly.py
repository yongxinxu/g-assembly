"""

The functions used to implement Lab 8 should be written here.
As usual, you'll need to include a test suite as well as your well-commented
functions.  In addition, you'll need to find any necessary code for doctest to
work (see past assignments) and import any needed libraries yourself.  After all,
other than this comment and a few tests below, this is a blank file!




########## Part 1: test suite ##########
>>> dot_matrix("hello", "jello")
array([[0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 0, 0, 1]])

# when len(seq) = 1:
>>> dot_matrix("h", "j")
array([[0]])

>>> dot_matrix("h", "h")
array([[1]])

# when len(seq) = 2:
>>> dot_matrix("hj", "yn")
array([[0, 0],
       [0, 0]])

>>> dot_matrix("hj", "hn")
array([[1, 0],
       [0, 0]])

>>> dot_matrix("hj", "jn")
array([[0, 0],
       [1, 0]])

>>> dot_matrix("hj", "hj") # overlap
array([[1, 0],
       [0, 1]])
       
# when len(seq) =5, and there is an overlap:
>>> dot_matrix("abcde", "cdefg") # 3-char overlap (seq_a:front, seq_b:end) # seq_a is put in the front and seq_b comes after it
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0]])

>>> dot_matrix("abcde", "defgc") # 2-char overlap (seq_a:front, seq_b:end)
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0]])
       
>>> dot_matrix("abcde", "bcdea") # 4-char overlap (seq_a:front, seq_b:end)
array([[0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0]])
       
>>> dot_matrix("bcdea", "abcde") # 4-char overlap (seq_a:end, seq_b:front)
array([[0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0]])

>>> dot_matrix("bcdea", "aedcb") # 5-char reverse overlap 
array([[0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0]])
       
>>> dot_matrix("bcdea", "baaed") # 3-char reverse overlap 
array([[1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0],
       [0, 1, 1, 0, 0]])

>>> dot_matrix("bcdea", "deabc") # 3-char overlap (seq_a:front, seq_b:end) and 2-char overlap (seq_a:end, seq_b:front)
array([[0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0]])

>>> dot_matrix("bcdea", "adebc") # 1-char overlap (seq_a:front, seq_b:end) and 2-char overlap (seq_a:end, seq_b:front)
array([[0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0]])
       
########## Part 2: test suite ##########
       
A sample test for part 2 of the lab.  The dictionary output order is not
guaranteed, so we test equality instead of directly testing the dictionary.

>>> amino_acids("tttttttggaga") == {'R': 1, 'W': 1, 'F': 2}
True

>>> amino_acids("catttc") == {'H': 1, 'F': 1}
True

>>> amino_acids("tttttttttttt") == {'F': 4}
True

>>> amino_acids("tatcatgtatatgggcat") == {'Y': 2, 'H': 2, 'G': 1, 'V': 1}
True

########## Part 3: test suite ##########
       
A sample test for part 3 of the lab, run on a small set of test fragments.
The final function should be able to run on the full set of fragments available
in genome_lib.get_fragments().


>>> put_fragments_together(get_test_fragments())
'ttttttggagacgcggg'

>>> put_fragments_together(['tttttt', 'ttttgg', 'tggaga', 'agacgc', 'cgcggg'])
'ttttttggagacgcggg'

>>> put_fragments_together(['tttttt', 'tttttt', 'tttttt', 'tttttt', 'tttttt'])
'tttttt'

>>> put_fragments_together(['ttagaaaa', 'aagctatt', 'ctgagatg', 'tattagct', 'gtatatgg'])
'ttagaaaagctattagctgagatgtatatgg'

>>> put_fragments_together([])
''

>>> len(put_fragments_together(get_fragments()))  # to get the length of the final fragment
42321

>>> count_overlap("bcdea", "baaed") # test suite for the helper function count_overlap
0

>>> count_overlap("tttct", "tttca")
1

>>> count_overlap("gcgaa", "aggtt")
1

>>> count_overlap("tatct", "tcgct")
1
     
>>> count_overlap("tatct", "ctgat")
2

>>> count_overlap("ttttt", "ttaaa")
2

>>> count_overlap("tatct", "tctat")
3

>>> count_overlap("ttttt", "tttaa")
3

>>> count_overlap("ttttt", "tttta")
4

>>> count_overlap("atcgt", "tcgta")
4
  
>>> count_overlap("tatct", "tatct")
5

>>> select_fragment('tttttt', ['ttttgg', 'tggaga', 'agacgc', 'cgcggg'], 6) # test suite for the helper function select_fragment
'ttttgg'

>>> select_fragment('ttttttgg', ['agacgc', 'tggaga', 'cgcggg'], 6)
'tggaga'

"""

from numpy import *
from genome_lib import *
#import traceback


# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    import traceback
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

# attempting to find error location
try:
    assert True
    assert 7 == 7
    assert 2 == 2
except:
    _,_, tb = sys.exec_info()
    traceback.print_tb(tb)   # fixed format
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    
    print('An error occurred on line {} in statement {}'.format(line,text))
    exit(1)



'''
# PART ONE
'''
#(a)   
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

def dot_matrix(seq_a, seq_b):
    assert (type(seq_a)==type(seq_b)==type("a string")) # sequences are strings
    assert len(seq_a)==len(seq_b) # the lengths of two sequences should be equal and greater than zero
    
    n = len(seq_a)
    answer = zeros([n,n], dtype=int) # create a two-dimensional array with all zeros 
    
    return equal_character(seq_a, seq_b, answer, 0)
    # postconditon: the result is the square matrix of the two sequences, in which the entry in the ith row and jth coloumn
    #               should be 0 if the ith character of the first sequence is not equal to the jth character of the second
    #               sequence and be 1 if these characters are equal. 

#(b)
'''
# If there is an overlap between two sequences, first, 1 appears in the dot_matrix, and if there are more than one character
# which overlap, there is a diagonal pattern of 1 from upper left to lower right at which the last 1 ends at the last row, and 
# if this diagonal has 1 in the first column,seq_b is overlapping to the end of seq_a; if the diagonal has 1 in the last column, 
# seq_a is overlapping to the end of seq_b; and if the diagonal starts and ends at the middle columns, there is only overlap in 
# the middle of two sequences, but two sequences cannot add to the end of each other. And if the diagonal pattern of 1 starts from 
# the upper right to the lower left, it means the reverse of a substring of one of the sequences matches the other. 

# cooperator: Mallory Kastner
'''
    
'''
# PART TWO
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
# PART THREE
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
 

 






                
# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
   
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    print "Running 'doctest' tests for graph coloring enumeration. These may take a little time..."
    print " To use the graphical interface, run A_graphical_user_interface.py"
    result = _test()
    if result[0] == 0:
        print "Congratulations! You have passed all" , result[1], "coloring enumeration tests"
    else:
        print "Rats!"   

