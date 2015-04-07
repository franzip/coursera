# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import sys, os, re
sys.path.append(re.sub('week\d$', 'lib', os.getcwd()))
import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent



## 1: (Task 1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u = list2vec([randGF2() for x in range(6)])
    if a0 * u == s and b0 * u == t:
        return u
    else:
        return choose_secret_vector(s, t)

from itertools import combinations

def generate_random_vecs():
    s, t = randGF2(), randGF2()
    while True:
        vecs = {(a0, b0)}
        for x in range(4):
            a = choose_secret_vector(s, t)
            b = choose_secret_vector(s, t)
            vecs.add((a, b))
        check_ind = [generate_vec_set(x) for x in combinations(vecs, 3)]
        if independent_vectors(check_ind):
            break
    return list(vecs)


def generate_vec_set(vec_tuple):
    return {vec_tuple[x][y] for x in range(len(vec_tuple)) for y in range(len(vec_tuple[x]))}


def independent_vectors(vecs):
    return all(is_independent(x) for x in vecs)

result = generate_random_vecs()

## 2: (Task 2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
secret_a0 = result[0][0]
secret_b0 = result[0][1]
secret_a1 = result[1][0]
secret_b1 = result[1][1]
secret_a2 = result[2][0]
secret_b2 = result[2][1]
secret_a3 = result[3][0]
secret_b3 = result[3][1]
secret_a4 = result[4][0]
secret_b4 = result[4][1]

