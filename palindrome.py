class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)  # Convert int to string
        reversed_s = x_str[::-1]
        return x_str == reversed_s