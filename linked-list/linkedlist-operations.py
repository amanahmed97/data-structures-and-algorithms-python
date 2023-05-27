import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        temp_list = []
        while temp:
            temp_list.append(temp.data)
            print(temp.data, "->", end=" ")
            temp = temp.next
        return temp_list

    def add(self, data):
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def add_list(self, arr):
        if len(arr) == 0:
            return None

        self.head = Node(arr[0])
        for x in arr[1:]:
            self.add(x)


# def main():
#     ip = [1, 2, 3]
#     ll = LinkedList()
#     ll.add_list(ip)
#     ll.print_list()
#
#
# if __name__ == '__main__':
#     main()


class Test(unittest.TestCase):
    def test_create(self):
        ip = [3, 2, 1]
        ll = LinkedList()
        ll.add_list(ip)
        self.assertEqual(ll.print_list(), ip)

    def test_create_single(self):
        ip = [3]
        ll = LinkedList()
        ll.add_list(ip)
        self.assertEqual(ll.print_list(), ip)

    def test_create_empty(self):
        ip = []
        ll = LinkedList()
        ll.add_list(ip)
        self.assertEqual(ll.print_list(), ip)
