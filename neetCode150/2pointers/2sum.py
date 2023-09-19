from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    # because of constant extra space
    s = 0
    b = 1
    somme = numbers[s] + numbers[b]
    while somme < target:
        if b == len(numbers) - 1:
            break
        b += 1
        somme = numbers[s] + numbers[b]
    while somme != target:
        if somme < target:
            s += 1
        if somme > target:
            b -= 1
        somme = numbers[s] + numbers[b]

    return [s + 1, b + 1]