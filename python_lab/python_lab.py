## Task 1
minutes_in_week = 24*7*60

## Task 2
remainder_without_mod = 2304811-2304811//47*47

## Task 3
divisible_by_3 = (673+909)%3==0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = {11, 19, 13}
Y1 = {23, 37, 43}

## Task 8: enter in the two new sets
X2 = { 2, 4, 8 }
Y2 = { 3, 6, 12 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {base**2*x+base*y+z for x in digits for y in digits for z in digits }

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {val for val in S if val in T}

## Task 11
L_average = sum([20,10,15,75])/len([20,10,15,75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum =sum([ sum(each) for each in LofL]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [[X,Y] for X in ['A','B','C'] for Y in [1,2,3]] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ (X,Y,Z) for X in S for Y in S for Z in S if X+Y+Z==0 ] 

## Task 15
exclude_zero_list = [(X,Y,Z) for X in S for Y in S for Z in S if X+Y+Z==0 and (X!=0 or Y!=0 or Z!=0)]

## Task 16
first_of_tuples_list = [(X,Y,Z) for X in S for Y in S for Z in S if X+Y+Z==0 and (X!=0 and Y!=0 and Z!=0)][0]

## Task 17
L1 = [1,2,3,3,4,5] # <-- want len(L1) != len(list(set(L1)))
L2 = [1, 20, 3, 5] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(0,100) if x%2!=0}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [sum(each) for each in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [each[k] for each in dlist]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [each.get(k,'NOT PRESENT') for each in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [each.get(k,'NOT PRESENT') for each in dlist] # <-- as you do here

## Task 23
square_dict =  {num:num**2 for num in range(0,100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {each:each for each in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {a:[int(a/(base**2)),int(a/(base)%base),int(a%(base))] for a in range(0,1000)}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {names[k]:v for (k,v) in d.items()}

## Task 27
def nextInts(L): return [ each+1 for each in L ]

## Task 28
def cubes(L): return [ each**3 for each in L ] 

## Task 29
def dict2list(dct, keylist): return [ dct[each] for each in keylist ]

## Task 30 
def list2dict(L, keylist): return dict(zip(keylist,L)) 

