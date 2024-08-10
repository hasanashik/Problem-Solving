# Problem:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Approach 1:

def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^0-9a-zA-Z]+', '', s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return self.isPalindrome(s[1:-1])

# Approach 2:
def isPalindrome(self, s: str) -> bool:
    def check_palindrome(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return check_palindrome(left + 1, right - 1)
    
    s = re.sub('[^0-9a-zA-Z]+', '', s.lower())
    
    return check_palindrome(0, len(s) - 1)
    
# Time Complexity: O(n)
# Space Complexity: O(n)
