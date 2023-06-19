import unittest
from collections import deque


def main2():
    q = deque()
    q.append(1)
    q.extend([2,3])
    print(q)
    q.appendleft(4)
    print(q)
    print(q.count(4))
    print(q.index(4))
    q.rotate(2)
    print(q)
    q.reverse()
    print(q)
    q.insert(1,7)
    print(q)
    q.popleft()
    q.remove(3)
    print(q)

def main():
    s = []
    s.append(1)
    s.append(2)
    s.append(3)
    print(s)
    s.pop()
    print(s)
    s.append(4)
    print(s)
    s.pop(0)
    print(s)


if __name__ == '__main__':
    main()
    main2()