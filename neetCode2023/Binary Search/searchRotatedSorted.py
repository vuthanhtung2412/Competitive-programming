from typing import List


def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        # NOTE : split case in the most intuitive way
        # determine if mid is in the left or right portion of the array first
        elif nums[l] <= nums[mid]:  # left
            if nums[l] < target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] <= nums[r]: # right
            if nums[mid] < target < nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1, 2, 3, 4, 5, 6], 4))
print(search([8, 1, 2, 3, 4, 5, 6, 7], 6))
print(search([4, 5, 6, 7, 8, 1, 2, 3], 8))
