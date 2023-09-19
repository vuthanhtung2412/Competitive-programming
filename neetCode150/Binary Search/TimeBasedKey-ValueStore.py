from typing import List


class TimeMap:

    def __init__(self):
        # time stamp always bigger for latter insertion
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            l = 0
            r = len(self.d[key]) - 1
            mid = 0
            if self.d[key][r][0] <= timestamp:
                return self.d[key][r][1]
            while l < r:
                if l + 1 == r:
                    if self.d[key][l][0] == timestamp:
                        return self.d[key][l][1]
                    elif self.d[key][l + 1][0] == timestamp:
                        return self.d[key][l + 1][1]
                    elif self.d[key][l][0] < timestamp:
                        return self.d[key][l][1]
                    else:
                        return ""

                mid = (l + r) // 2
                if self.d[key][mid][0] == timestamp:
                    return self.d[key][mid][1]
                # because the target can be in the middle of mid and mid + 1
                elif timestamp < self.d[key][mid][0]:
                    r = mid
                else:
                    l = mid
        else:
            return ""


def fun(nums: List[int], target) -> int:
    l = 0
    r = len(nums) - 1
    mid = 0
    if nums[r] <= target:
        return r
    while l <= r:
        if l + 1 == r:
            if nums[l] == target:
                return l
            elif nums[l + 1] == target:
                return l + 1
            elif nums[l] < target < nums[l + 1]:
                return l
            else:
                break

        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid
        else:
            l = mid

    return -1


arr = [1, 4]
print(fun(arr, 5))
