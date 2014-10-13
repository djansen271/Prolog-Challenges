'''
Experimenting on 1.07
with generators
'''

def createGenerator():
    mylist = range(8)
    for i in range(5):
        yield i*i

mygenerator = createGenerator()
print (mygenerator)
for j in mygenerator:
    print j

secondgenerator = createGenerator()
for i in secondgenerator:
    print i