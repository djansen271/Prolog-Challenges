"""
1.01 (*) Find the last element of a list.
Example:
?- my_last(X,[a,b,c,d]).
X = d
"""
"""
my_last(a_list) receives a list as an input
it returns the last element of the list using the pop function
"""
def my_last(a_list):
    if a_list == []:
        return ''
    else:
        return a_list.pop()


Q = [3,4,5,6]
print my_last(Q)
r = []
print my_last(r)