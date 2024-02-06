import sys
from collections import *

b = [3,1,[1,2]]
a = [3,1]

# print(struct.pack("b"*len(a), *a))
print(len(bytes(a)))

print(sys.getsizeof(a))


d = defaultdict(list)

# l = d.get('a',[])
# print(l)

a = "abc"
b = "bcd"

# l.append(a)
# print(l)
d[a].append(a)
# l.append(b)
# print(l)

print(d)


def groupAnagrams(strs):
    ans = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    print(ans)
    return ans.values()

print(groupAnagrams(["abc","cba","tea","ate"]))

"""
dictionary of integers
"""
a = defaultdict(int)
a[1]+=5
print(a[2])
# op:  defaultdict(<class 'int'>, {1: 5})

"""
array methods
"""
a = [8,9,7]
print(a.index(7))
a.remove(7)
print(a)
# [8, 9]
print(Counter(a))
# Counter({8: 1, 9: 1})


print(divmod(4,9))

print(ord('a'))
print(chr(97))

print(-20%60)

print((7).bit_count())
print(bin(8))

y = lambda x: x*10
l = [lambda arg=x: arg*10 for x in b]
print(l[0]())

