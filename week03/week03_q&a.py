# shallow copy, deep copy
import copy

a = [1, [3,-9],4]
# a[1][0] = 55
print(a)
b = a
c = a.copy()
d = a[:]
e = copy.deepcopy(a)
b[1][0] = 55
print(b)
print(c)
print(d)
print(e)