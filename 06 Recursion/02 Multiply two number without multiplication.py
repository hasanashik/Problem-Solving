class Solution:
    def multiply(self, a: int, b: int) -> int:
        if b == 0:
            return 0
        
        return a + self.multiply(a, b - 1)

# time & space complexity: O(len(b))
 