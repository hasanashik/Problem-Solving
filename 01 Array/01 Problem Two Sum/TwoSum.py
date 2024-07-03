from typing import List


class CustomMap:
    def __init__(self):
        self._map = {}

    def _hash(self, key):
        return hash(key)

    def has(self, key):
        hashed_key = self._hash(key)
        return hashed_key in self._map

    def set(self, key, value):
        hashed_key = self._hash(key)
        self._map[hashed_key] = value

    def get(self, key):
        hashed_key = self._hash(key)
        if hashed_key in self._map:
            return self._map[hashed_key]
        return None


def twoSum(nums: List[int], target: int) -> List[int]:
    map = CustomMap()
    for i, num in enumerate(nums):
        need = target - num
        if map.has(need):
            return [map.get(need), i]
        map.set(num, i)


if __name__ == '__main__':
    input_string = input("Enter nums & target: ")
    # Find nums
    nums = []
    nums_temp = input_string.strip().split('nums =')[1].strip().split(', target')[
        0].replace('[', '').replace(']', '').split(',')
    for item in nums_temp:
        nums.append(int(item))
    # Find target
    target = int(input_string.strip().split('target =')[1].strip())
    output = twoSum(nums, target)
    print(output)

    #  Time Complexity: O(len(nums))
    #  Space Complexity: O(len(nums))
