"""
Merge Sort

Time Complexity: O(nlogn)
"""


def merge(arr1, arr2):
    p1 = 0
    p2 = 0    
    arr = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            # print(f"p1:{p1}")
            # print("arr1: {} \n arr2: {}".format(arr1, arr2))
            arr.append(arr1[p1])
            p1 = p1 + 1            
        elif arr2[p2] < arr1[p1]:
            arr.append(arr2[p2])
            p2 = p2 + 1            
        elif arr1[p1] == arr2[p2]:
            arr.append(arr1[p1])
            arr.append(arr2[p2])
            p1 = p1 + 1
            p2 = p2 + 1            

    if p1 < len(arr1):
        while p1 < len(arr1):
            arr.append(arr1[p1])
            p1 = p1 + 1            
    if p2 < len(arr2):
        while p2 < len(arr2):
            arr.append(arr2[p2])
            p2 = p2 + 1            

    return arr

def merge_sort(a):
    # Return if array has just 1 element
    if len(a) == 1:
        return a

    # Split array into 2 halves
    arr1 = a[:int(len(a) / 2)]
    arr2 = a[int(len(a) / 2):]
    print("arr1: {}  arr2: {}".format(arr1,arr2))
    # Recursively sort the sub arrays
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    # Return merged sorted sub arrays
    return merge(arr1, arr2)


a = [9, 5, 6, 3, 2, 0, -1]
b = merge_sort(a)
print("Sorted:")
print(b)
