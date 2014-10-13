# -*- coding: utf-8 -*-
'''
1.02 (*) Find the last but one element of a list.
(de: zweitletztes Element, fr: avant-dernier élément)
'''

def penult (lista):
    try:
        return lista[-2]
    except:
        return 'There is no penultimate element.'



q = []
print penult(q)
r = ['apple','banana','cucumber']
print penult(r)
s = ['apple','banana','cucumber', 'doughnut']
print penult(s)
t = ['apple']
print penult(t)

for i in [q,r,s,t]:
    print penult(i)