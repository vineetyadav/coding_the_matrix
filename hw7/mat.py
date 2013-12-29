from vec import Vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    if k in M.f.keys():
        return M.f[k]
    else:
        return 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    return_Mat = Mat(A.D,{})
    assert A.D == B.D
    for each in A.f:
        if each in B.f.keys():
            return_Mat.f[each] = A.f[each]+B.f[each]
    for each in A.f:
        if each not in B.f.keys():
            return_Mat.f[each] = A.f[each]
    for each in B.f:
        if each not in A.f.keys():
            return_Mat.f[each] = B.f[each]
    return return_Mat

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M"
    return_Mat = Mat(M.D,{})
    for each in M.f.keys():
        return_Mat.f[each] = alpha*M.f[each]
    return return_Mat

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    for each in A.f:
        if each in B.f.keys():
            if A.f[each]!=B.f[each]:
                return False
        elif A.f[each]!=0:
            return False
    for each in B.f:
        if each not in A.f.keys():
            if B.f[each]!=0:
                return False
    return True

def transpose(M):
    "Returns the transpose of M"
    return_Mat = Mat((M.D[1],M.D[0]),{})
    for each in M.f:
        return_Mat.f[each[1],each[0]] = M.f[each]
    return return_Mat

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    return_vec = Vec(M.D[1],{})
    #for each in return_vec.f:
    #    return_vec[each] = 0
    
    assert M.D[0] == v.D
    for row in M.D[0]:
        for col in M.D[1]:
            if row in v.f.keys():
                return_vec[col] = return_vec[col]+v[row]*M[row,col]
    return return_vec

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    return_vec = Vec(M.D[0],{}) 
    #for each in v.f:
    #    return_vec[each] = 0
    
    for row in M.D[0]:
        for col in M.D[1]:
            if col in v.f.keys():
                return_vec[row] = return_vec[row]+v[col]*M[row,col]
    return return_vec

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    return_Mat = Mat((A.D[0],B.D[1]),{})
    for row in A.D[0]:
        for col in B.D[1]:
            for temp in A.D[1]:
                return_Mat[row,col] = return_Mat[row,col]+A[row,temp]*B[temp,col]
    return return_Mat

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
