def insertion_sort(a):
    for j in range(1, len(a)):
        print(f"j: {j}")
        key = a[j]
        print("key: {}".format(key))
        i = j - 1
        while i >= 0 and a[i] > key:
            # print(f"i: {i}")
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a


a = [9, 5, 6, 3, 2, 0, -1]
b = insertion_sort(a)
print("Sorted:")
print(b)