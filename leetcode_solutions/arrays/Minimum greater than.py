"""

Given a number n, find the smallest number that has same set of digits as n and is greater than n.
1234  -> 1243

218765 -> 251678  , 216578
258761

2421 -> 4122

2 421
4 221
4 122


218765
21 8765
25 8761
25 1678

21 5678
25 1678
"""


def greater_than(n):
    nums = []

    for v in str(n):
        nums.append(int(v))

    print(nums)
    r = len(nums) - 2
    while nums[r] > nums[r + 1]:
        r -= 1
    print(nums[r], r)

    sorted_array = nums[r + 1: len(nums) + 1]
    # print(sorted_array)
    sorted_array.sort()
    print(sorted_array)

    i = 0
    while i < len(sorted_array):
        if sorted_array[i] > nums[r]:
            # print(sorted_array[i], r)
            nums[r], sorted_array[i] = sorted_array[i], nums[r]
            break
        i += 1
    sorted_array.sort()

    i = r + 1
    j = 0
    while i < len(nums):
        nums[i] = sorted_array[j]
        i += 1
        j += 1

    print(nums)
    # nums = ''.join
    # return


greater_than(218765)
