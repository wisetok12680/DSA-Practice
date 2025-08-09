class Solution(object):
    def singleNumber(self, nums):
        result=0
        for num in nums:
            result^=num
        return result

#using XOR operation to find the single number
