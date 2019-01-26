# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import numpy as np


def solution(S, K):
    # write your code in Python 3.6
    N = len(S)
    # string = ["" for _ in range(N)]
    string = []
    N = N - 1
    t = 0

    for i in range(N, -1, -1):

        if S[i].isalpha():
            string.append(S[i].upper())
            t = t + 1
        elif S[i].isdigit():
            string.append(S[i])
            t = t + 1
        else:
            pass
        if t >= K and i > 0:
            t = 0
            string.append("-")
    s = "".join(reversed(string))
    return s


# test code above
S = "2-4A0r7-4k"
K = 3
# print(solution(S, K))


## some coomon tricks in python:

# 1.*** reverse indexing for a str of len 10:range([start], stop[, step])

# for i in range(9, -1, -1):
#     print(i)




#2. *** to split str s into its chars
# s = "abc"
# lst = list(s)
# print(s)

#3. *** using map : function will be applied to all elments of s
# lst = list(map(lambda c: c if c.isalpha() else "", s))
# print(lst)


#4. *** using sort in dict
# d = {"vcb": 1, "ced": 2}
# d2 = sorted(d.items(), key=lambda x: x[0][1])
# print(d2)


# 5. *** using numpy
L = [1, 2, 21]
x = L[np.where(L > 2)]

some_text1 = "vsba"
some_text2 = "fara"
# np_arr = np.array(list(some_text), dtype=str)
np_arr1 = np.array(list(some_text1))
np_arr2 = np.array(list(some_text2))
np_arr1 = np.core.defchararray.add(np_arr1, np_arr2)
np_arr1.view((str, 1))
# np_arr = np.chararray(len(some_text))
# np_arr1[0:3] = "salam"
# arr = np.array_str(np_arr)
# arr = np_arr1[np.where(np_arr1, np_arr1, "")]
# f = lambda x: x.isupper()
# np_arr = list(np.array(map(f(np_arr), np_arr)))
# print(np_arr1.astype(dtype=str))

# np_arr1.add(np_arr12)
print(np_arr1)
#
#
# def slicer_vectorized(a,start,end):
#     b = a.view((str, 1)).reshape(len(a), -1)[:, start:end]
#     print(a.view((str, 1)))
#     print(b.tostring())
#     return np.fromstring(b.tostring(), dtype=(str, end-start))
#
# a = np.array(['hello', 'how', 'are', 'you'])
# print(slicer_vectorized(a, 1, 3))


code = "2-4A0r7-4k"
num =4
arr1 = np.array(list(code), dtype=np.unicode_)
f = lambda x: np.core.defchararray.isalpha(x) | np.core.defchararray.isdigit(x)
# arr = arr[np.where(f(arr), arr, "")]
arr2 = f(arr1)
# arr = arr[np.where(arr is True, arr, "")]
arr2 = np.where(arr2, arr1, "")

# arr2[-1*num] = "-"
# np.core.defchararray.

print(arr2)


### *** deiffernce between isnumeric and ...
# def spam(s):
#    for attr in 'isnumeric', 'isdecimal', 'isdigit':
#        print(attr, getattr(s, attr)())
#
# print(spam("½"))
#
#



### 6. *** using a mthod vs getattr()
# lst = [1, 2, 3]
# 1 and 2 are equivalanet
# 1. print(getattr(lst, "pop")())
# 2. lst.pop()
#    print(lst)



#7. *** using filter, map, enumerare
# print(list(filter(func, [2, 3])))
# print(list(map(some_f, lst)))
# lst = [1, 2, 3]
#it = iter(enumerate(lst))
# so then I can call the elemts in it by two ways:

#1.
# while it.__next__():
#     print(1)

# 2. el = it.__next__()


#8.  reversing an str
# s = "".join(reversed(string))


#9.
# def __eq__(self, other):
#     """Override the default Equals behavior"""
#     if isinstance(other, self.__class__):
#         return self.color == other.color and self.size == other.size
#     return False


###10. round a number num to the neaset 1000 from above
# rounded_num = math.ceil(value / 1000) * 1000
## form below
# rounded_num = math.floor(value / 1000) * 1000


def countDuplicates(numbers):
    # Write your code here

    d= {}
    count = 0
    for n in numbers:
        if n in d:
            d[n] = 2
            count += 1
        else:
            d[n] = 1
    d.values()

    return count



li = [1, 2,2, 3,3,3]

print(countDuplicates(li))
