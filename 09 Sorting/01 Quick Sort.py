def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] >= pivot:  
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def quickselect(nums, left, right, k):
    if left <= right:
        pivot_index = partition(nums, left, right)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index > k:
            return quickselect(nums, left, pivot_index - 1, k)
        else:
            return quickselect(nums, pivot_index + 1, right, k)
    return -1

def parse_input(input_str):
    input_str = input_str.strip()
    nums_str = input_str[input_str.index('['):input_str.index(']')+1]
    nums = eval(nums_str)
    k_str = input_str[input_str.index('k =') + 3:].strip()
    k = int(k_str)
    return nums, k
    
def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, k - 1)

# input_str = "nums = [3,2,1,5,6,4], k = 2"
nums, k = parse_input(input())
print(findKthLargest(nums, k))


# Time Complexity: O(n)  worst case O(n^2)
# Space Complexity: O(1)