'''
1.06 (*) Find out whether a list is a palindrome.
A palindrome can be read forward or backward; e.g. [x,a,m,a,x].
'''

def reverse(listd):  #this is from 1-5
    listb =[]
    lista = list(listd) #equivalent to lista = listd[:] makes a copy of listd
    k = len(lista)
    for i in range(k):
        #print "i="+str(i)
        #print "lista="+ str(lista)
        listb.append(lista.pop())
        #print "listb="+str(listb)
    return listb

def compare(listb, listc):
    '''If the two lists are the same, returns "same." If two lists are not 
    the same, returns "notsame".
    '''
    if len(listb) != len(listc):
        return "notsame"
    for i in range (len(listb)):
        if listb[i] != listc[i]:
            return "notsame"
    return "same"

def palindrome (listf):
    if compare(listf,reverse(listf)) == 'notsame':
        print "Not a palindrome."
    else: 
        print "Palindrome!"
    return ""
q = ['a','b','c','b','a']
r = [0,1,2,3,4,5,4,3,2,1,0]
s = [1,2,3,4]
t = [1,2,3,4,3,2,1]
u = [1,2,3,]
        
for i in (q,r,s,t):
    print i,palindrome(i)         