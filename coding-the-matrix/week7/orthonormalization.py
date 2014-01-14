from orthogonalization import orthogonalize
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    temp = orthogonalize(L)
    norms = []
    for x in range(len(temp)):
        sqr = 0
        for y in temp[x].D:
            sqr += getitem(temp[x],y)**2
        norms.append(sqr)
    for x in norms:
        x = math.sqrt(x)
    return [norms[x] * L[x] for x in range(len(L))]

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    pass
