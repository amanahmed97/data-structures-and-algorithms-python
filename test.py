import sys

b = [3,1,[1,2]]
a = [3,1]

# print(struct.pack("b"*len(a), *a))
print(len(bytes(a)))

print(sys.getsizeof(a))