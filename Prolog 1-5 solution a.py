'''
1.05 (*) Reverse a list.
'''

def reverse(lista):
    listb =[]
    k = len(lista)
    for i in range(k):
        #print "i="+str(i)
        #print "lista="+ str(lista)
        listb.append(lista.pop())
        #print "listb="+str(listb)
    return listb

q = [1,2,3,4,5]
print reverse(q)
r = []
print reverse(q)
q = [1,2,3,4,5,'a','b','c','d','e']
print reverse(q)