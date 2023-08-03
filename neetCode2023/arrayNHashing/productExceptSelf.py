from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    # 2 0 in the list
    count = 0
    prod = 1
    for i in nums:
        if i == 0:
            count += 1
            if count > 1:
                return [0] * len(nums)
        else:
            prod *= i

    if count == 1:
        return [0 if i != 0 else prod for i in nums]

    return [int(prod / i) for i in nums]

print(productExceptSelf([-1,1,0,-3,3]))