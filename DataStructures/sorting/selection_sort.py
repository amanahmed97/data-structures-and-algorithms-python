"""
Selection Sort

Time Complexity: O(n^2)
"""


def selection_sort(nums):
    if not nums:
        return nums

    for i in range(len(nums)):
        idx=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[idx]:
                idx = j
        temp = nums[i]
        nums[i] = nums[idx]
        nums[idx] = temp

    return nums


nums = [5,4,3,-2,1]

answer = selection_sort(nums)
print(answer)
