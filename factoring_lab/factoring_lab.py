from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    if i%2==0:
        return 0
    else:
        return one

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return_vec = Vec(primeset,{})
    for each in factors:
        return_vec.f[each[0]] = int2GF2(each[1])
    return return_vec

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots=[]
    rowlist=[]
    y=0
    b=0
    #c = []
    #d = []
    c=len(primeset) +1
    i =2
    #j=range(i)
    #for x in j:
    #    y=intsqrt(N)+x
    #    a=dumb_factor(y*y-N,primeset)
    #    if a!=[]:
    #        c.append(y)
    #        d.append(make_Vec(primeset,a))
            #i=i+len(c)+len(d)
    #for x in range(i):
    #for x in primeset:
    while( len(roots)<=c):
        if i!=0 and i!=1:
            y=intsqrt(N)+i
            i = i +1
            a=dumb_factor(y*y-N,primeset)
            if a!=[]:
                #c.append(y)
                #d.append(make_Vec(primeset,a))
                roots.append(y)
                
                rowlist.append(make_Vec(primeset,a))
    return (roots,rowlist)



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [roots[i] for i in range(len(roots)) if v[i] != 0]
    a = prod(alist)
    c = prod(x*x-N for x in alist)
    b = intsqrt(c)
    assert b*b ==c
    return (a,b)

## Task 5
N = 2461799993978700679
primeset = primes(10000)
roots,rowlist = find_candidates(N,primentset)
M = echelon.transformation_rows(rowlist, sorted(primeset, reverse=True)) # 320 s
for v in M[::-1]:
    a,b = find_a_and_b(v,roots,N)
    
smallest_nontrivial_divisor_of_2461799993978700679 = ... 
