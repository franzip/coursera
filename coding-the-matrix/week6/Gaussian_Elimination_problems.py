# version code 62505f329d9b
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import sys, os, re
sys.path.append(re.sub('week\d$', 'lib', os.getcwd()))
from matutil import *
from GF2 import one
from vecutil import zero_vec


## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 4]]

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]


## 2: (Problem 2) Is it echelon?
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
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[1,1,1],[0,1,0],[0,0,0],[0,0,0]])
        True
        >>> is_echelon([[1,1,1],[0,1,0],[0,0,0],[0,0,0], [0,0,0]])
        True
        >>> is_echelon([[1,1,1],[0,0,0],[0,0,1]])
        False
    '''
    def compute_zero_pos(L):
        result = -1
        for x in range(len(L)):
            if L[x] != 0:
                return result
            result = x
        return result

    def all_zeros(L):
        return all(map(lambda el: el == 0, L))

    def check(A, idx, zero_pos, zero_row):
        current_row  = A[idx]
        current_zero = compute_zero_pos(current_row)
        # last row check
        if idx == len(A) - 1:
            # check zero_row flag
            return all_zeros(current_row) if zero_row else current_zero > zero_pos
        zero_row = all_zeros(current_row)
        # we met a zero row, recurse checking if next rows are zero rows
        if zero_row:
            return all_zeros(current_row) and check(A, idx + 1, current_zero, zero_row)
        # no zero row so far, keep recursing normally
        return check(A, idx + 1, current_zero, zero_row) if current_zero > zero_pos else False

    return True if len(A) <= 1 else check(A, 0, -2, False)


## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]


## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## 5: (Problem 5) Echelon Solver
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    '''
    D = label_list
    x = zero_vec(row_list[0].D)
    b_len = len(row_list)
    for j in reversed(range(len(row_list))):
        c = label_list[j]
        row = row_list[j]
        try:
            x[c] = (b[j] - x * row) / row[c]
        except ZeroDivisionError:
            pass
    return x


D = {'A', 'B', 'C', 'D'}
## 6: (Problem 6) Solving General Matrices via Echelon
row_list = [Vec(D, {'A':one, 'B':one, 'D':one}), Vec(D, {'B':one}), Vec(D, {'C':one}), Vec(D, {'D':one})]  # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D']  # Provide as a list
b = [one, 0, one, 0]          # Provide as a list of GF(2) values



## 7: (Problem 7) Nullspace A
null_space_rows_a = {3, 4} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {4} # Put the row numbers of M from the PDF

