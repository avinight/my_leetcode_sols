# First Answer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = ''
        for ch in str(x):
            rev = ch + rev
        return rev == str(x)
    
# Faster Answer
class Solution:
def isPalindrome(self, x: int) -> bool:
    x = str(x)
    if x == x[::-1]:
        return True
    return False
