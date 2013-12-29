# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from solver import solve


## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[ 1,0,0,1],
                  [0,0,0,1 ],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    return True if len(A) < 2 else all([(lambda V, k, s: V[k] > V[k-1] if V[k] != s else True)([next((i for i in range(len(r)) if r[i] != 0), len(r)) for r in A], k, len(A[0])) for k in range(1, len(A))])



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-4,-1,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [1,10,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    
    M = rowdict2mat(rowlist)
    v = Vec(M.D[0],{j:b[j] for j in range(len(M.D[0]))})
    s = solve(M,v)
    solve.__calls__ = 0
    return s



## Problem 6
#rowlist = [Vec({ 'A', 'B', 'C', 'D'}, {'A':one, 'B':one, 'D':one}), Vec({'A','B','C','D'},{'A':one, 'D':one}), Vec({'A','B','C','D'},{'A':one,'B':one,'C':one,'D':one}),Vec({'A','B','C','D'},{'C':one,'D':one}) ]    # Provide as a list of Vec instances
rowlist =[Vec({'A', 'B', 'C', 'D'}, {'A': one, 'B': one, 'D': one}), Vec({'A', 'B', 'C', 'D'}, {'B': one, 'C': one}), Vec({'A', 'B', 'C', 'D'}, {'C': one, 'D': one}), Vec({'A', 'B', 'C', 'D'}, {'D': one})]    # Provide as a list of Vec instances
label_list = ['A','B','C','D'] # Provide as a list
b = [one, one, 0.000000, 0.000000]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

#project_onto_2 = [-0.16666666666666666, -0.33333333333333331, 0.16666666666666666]
#projection_orthogonal_2 = [1.1666666666666667,2.3333333333333335,3.8333333333333335]

project_onto_2 = [-1/6.0, -1/3.0, 1/6.0]
projection_orthogonal_2 = [1+1/6.0,1+1/3.0,4-1/6.0]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

