class Solution(object):
    def maximumWealth(self, accounts):
        total=[]
        for num in accounts:
            total.append(sum(num))
        return max(total)