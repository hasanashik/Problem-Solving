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

    def isValid(self, s: str) -> bool:
        our_stack = self.Stack()
        parentheses = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in ['(', '{', '[']:
                # push in stack
                our_stack.push(char)
            if char == ')' or char == '}' or char == ']':
                # check stack first item opposite paranthesis or not
                if our_stack.peek() != parentheses[char]:
                    return False
                else:
                    our_stack.pop()
        if our_stack.is_empty():
            return True
        else:
            return False


if __name__ == "__main__":
    result = Solution()
    print(result.isValid(input("Enter String: ")))
