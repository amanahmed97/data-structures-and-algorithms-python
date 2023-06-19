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
        print("")
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

    def delete(self, data):
        prev = self.head
        temp = prev.next

        # Check first element
        if prev.data == data:
            prev.next = None
            self.head = temp
            return True

        while temp:
            if temp.data == data:
                prev.next = temp.next
                return True
            prev = temp
            temp = temp.next

        return False

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

    def test_delete(self):
        ip = [3, 2, 1, 5]
        op = [3, 2, 5]
        ll = LinkedList()
        ll.add_list(ip)

        self.assertEqual(ll.delete(1), True)
        self.assertEqual(ll.print_list(), op)

    def test_delete_last(self):
        ip = [3, 2, 1, 5]
        op = [3, 2, 1]
        ll = LinkedList()
        ll.add_list(ip)

        self.assertEqual(ll.delete(5), True)
        self.assertEqual(ll.print_list(), op)

    def test_delete_first(self):
        ip = [3, 2, 1, 5]
        op = [2, 1, 5]
        ll = LinkedList()
        ll.add_list(ip)

        self.assertEqual(ll.delete(3), True)
        self.assertEqual(ll.print_list(), op)

    def test_delete_single(self):
        ip = [3]
        op = []
        ll = LinkedList()
        ll.add_list(ip)

        self.assertEqual(ll.delete(3), True)
        self.assertEqual(ll.print_list(), op)
