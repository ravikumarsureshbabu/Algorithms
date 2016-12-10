


def next_permutation(perm):

    perm[1],perm[2] = perm[2],perm[1]

   
    if perm[1] <= perm[2] :
        if perm[0] > perm[1] and perm[0] > perm[2]:
            perm[0],perm[2] = perm[2],perm[0]
            perm[0],perm[1] = perm[1],perm[0]
        elif perm[0] < perm[1] and perm[0] < perm[2]:
            perm[0],perm[1] = perm[1],perm[0]
        else:
            perm[0],perm[2] = perm[2],perm[0]

   

a = [5,1,1]
next_permutation(a) 
print(a)
         
