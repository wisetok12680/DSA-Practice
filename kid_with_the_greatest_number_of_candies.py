class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most_candies = max(candies)
        final_result = []
        for num in candies:
            final_result.append(num + extraCandies >= most_candies)
        return final_result