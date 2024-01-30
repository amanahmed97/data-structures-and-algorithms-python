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
