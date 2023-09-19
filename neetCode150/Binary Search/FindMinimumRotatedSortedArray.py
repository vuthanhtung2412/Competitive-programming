from typing import List


def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    mid = 0
    # without this line the time will increase greatly because each iteration it has to initialize and terminate new variable which take up space and time
    if r == 0:
        return nums[0]
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] < nums[mid + 1] and l + 1 == r:
            return nums[mid]
        elif nums[mid] > nums[r]:
            l = mid
        else:
            r = mid


print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11, 13, 15, 17]))
print(findMin([3, 1, 2]))
print(findMin([2, 3, 4, 5, 1]))
