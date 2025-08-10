class Solution(object):
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
# This code uses bit manipulation to find the unique number in an array where every other number appears three times.