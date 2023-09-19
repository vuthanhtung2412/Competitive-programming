from typing import List
def search(nums: List[int], target: int) -> int:
    def recur(s: int, e: int):
        if s <= e:
            if nums[(e + s) // 2] == target:
                return (e + s) // 2
            elif nums[(e + s) // 2] > target:
                return recur(s, (s + e) // 2 - 1)
            elif nums[(e + s) // 2] < target:
                return recur((s + e) // 2 + 1, e)
        else:
            return -1