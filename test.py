
import numpy as np

## some coomon tricks in python:

# 1.*** reverse indexing for a str of len 10:range([start], stop[, step])

for i in range(9, -1, -1):
    print(i)

#2. *** to split str s into its chars
s = "abc"
lst = list(s)
print(s)

#3. *** using map : function will be applied to all elments of s
lst = list(map(lambda c: c if c.isalpha() else "", s))
print(lst)


#4. *** using sort in dict
d = {"vcb": 1, "ced": 2}
d2 = sorted(d.items(), key=lambda x: x[0][1])
print(d2)


# 5. *** using numpy
L = [1, 2, 21]
x = L[np.where(L > 2)]

some_text1 = "vsba"
some_text2 = "fara"


### 6. *** using a mthod vs getattr()
lst = [1, 2, 3]
1 and 2 are equivalanet
1. print(getattr(lst, "pop")())
2. lst.pop()
   print(lst)



#7. *** using filter, map, enumerare
print(list(filter(func, [2, 3])))
print(list(map(some_f, lst)))
lst = [1, 2, 3]
it = iter(enumerate(lst))
so then I can call the elemts in it by two ways:
#1.
while it.__next__():
    print(1)

#2. 
el = it.__next__()


#8.  reversing an str
s = "".join(reversed(string))


#9. eq method
def __eq__(self, other):
    """Override the default Equals behavior"""
    if isinstance(other, self.__class__):
        return self.color == other.color and self.size == other.size
    return False


###10. round a number num to the neaset 1000 from above
rounded_num = math.ceil(value / 1000) * 1000
# form below
rounded_num = math.floor(value / 1000) * 1000

## 11. deiffernce between isnumeric and ...
def spam(s):
   for attr in 'isnumeric', 'isdecimal', 'isdigit':
       print(attr, getattr(s, attr)())

print(spam("½"))

