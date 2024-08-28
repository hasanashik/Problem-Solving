# Problem statement: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
class Solution:
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            return None

        def peek(self):
            if not self.is_empty():
                return self.stack[-1]
            return None

        def is_empty(self):
            return len(self.stack) == 0

        def size(self):
            return len(self.stack)

    def removeDuplicates(self, s: str) -> str:
        result = ''
        if len(s) == 1:
            return s

        our_stack = self.Stack()
        our_stack.push(s[0])
        for char in s[1:]:
            if char != our_stack.peek():
                our_stack.push(char)
            else:
                our_stack.pop()

        for _ in range(our_stack.size()):
            result = result + our_stack.pop()

        return result[::-1]


if __name__ == "__main__":
    result = Solution()
    print(result.removeDuplicates(input("Enter String: ")))
    #  Time Complexity: O(string_length) and
    #  Space Complexity: O(string_length)
