class Solution(object):
    def numIdenticalPairs(self, nums):
        result=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    result+=1
        return result
        


#Efficient Version O(n) 
#HASH MAP

class Solution:
    def numIdenticalPairs(self, nums):
        count=0
        freq = {}

        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1

        return count