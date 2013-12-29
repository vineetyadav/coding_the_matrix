# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    #return all(is_independent( x ) for x in combinations(pairs,3))
    #all(is_independent(list(sum(x,()))) for x in combinations(L,3))
    #new_u=list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    #ua=a0.new_u
    #a0*new_u
    #b0*new_u
    #ub=b0.new_u
    #if ua == s and ub == t:
    #   return new_u
    #else:
    #    choose_secret_vector(s,t)
    a = [one, one,   0, one,   0, one]
    b = [one, one,   0,   0,   0, one]
    u = [randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()]
    dot_a = sum([a[i]*u[i] for i in range(6)])
    dot_b = sum([b[i]*u[i] for i in range(6)])
    if dot_a == s and dot_b == t:
        return list2vec(u)
    else:
        return choose_secret_vector(s,t)
## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
secret_a1 = ...
secret_b1 = ...
secret_a2 = ...
secret_b2 = ...
secret_a3 = ...
secret_b3 = ...
secret_a4 = ...
secret_b4 = ...

