class Solution(object):
    def singleNumber(self, nums):
        xor_all=0
        for num in nums:
            xor_all^=num
        rightmost_set_bit = xor_all & -xor_all
        num1 = 0
        num2 = 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num  
            else:
                num2 ^= num
        return num1,num2
    
#using XOR operation to find the two unique numbers in an array where every other number appears twice