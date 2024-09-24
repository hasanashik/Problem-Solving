class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        output = None
        
        low = 0
        high = length-1
        middle_index = (low + high)//2
        
        while True:
            print(low,high,middle_index)
            if low > high :
                return -1
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                low = middle_index + 1
            elif nums[middle_index] > target:
                high = middle_index - 1
            middle_index = (low + high)//2

# [-1,0,3,5,9,12] 9