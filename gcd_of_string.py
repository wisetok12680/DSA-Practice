class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2==str2+str1:
            a=len(str1)
            b=len(str2)
            while b != 0:  #Euclidean Algorithm used
                temp = b   # Example: GCD(48, 18) → 48 % 18 = 12 → 18 % 12 = 6 → 12 % 6 = 0 → GCD = 6
                b = a % b
                a = temp
            return str2[:a]
        else:
            return ""