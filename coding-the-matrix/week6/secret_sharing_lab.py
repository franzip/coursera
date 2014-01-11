# version code 988
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from vec import Vec
from vecutil import list2vec
import random
from hw5 import my_is_independent



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    global a0, b0
    randvec = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    if a0 * randvec == s and b0 * randvec == t:
        return u
    else:
        return choose_secret_vector(s, t)



## Problem 2
# Give each vector as a Vec instance
secret_a0 = list2vec([one, one, 0, one, 0, one])
secret_b0 = list2vec([one, one, 0, 0, 0, one])
secret_a1 = ...
secret_b1 = ...
secret_a2 = ...
secret_b2 = ...
secret_a3 = ...
secret_b3 = ...
secret_a4 = ...
secret_b4 = ...

