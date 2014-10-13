'''
1.03 (*) Find the K'th element of a list.
The first element in the list is number 1.
Example:
?- element_at(X,[a,b,c,d,e],3).
X = c
'''

def findk(lista,k):
    try:
        return lista[k]
    except:
        return "Sorry--can't do it"
q = []
r = [1,2,3,4,5,6,7,8]
s = [0,1,2,3,4,5,6,7,8]

for i in range (10):
    print findk(q,i)
    print findk(r,i)
    print findk(s,i)