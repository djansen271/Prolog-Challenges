'''
1.04 (*) Find the number of elements of a list.
'''

def findNumElem(lista):
    count = 0
    for i in (lista):
        count += 1
    return count
    
q = []
r = [1,2,3,4]
s = [1,2,3,[4,5,6]]
t = ['q',3,12]
u = (2,3,4,5)

for j in (q,r,s,t,u):
    print findNumElem(j)