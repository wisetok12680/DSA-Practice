class Solution(object):
    def reverse(self, x):
        pos_int = abs(x)                      
        s = str(pos_int)                      
        reversed_s = s[::-1]                  
        reversed_int = int(reversed_s)        

        if reversed_int > 2**31 - 1:         
            return 0
        if x<0:
            return reversed_int*-1
        else:
            return reversed_int
        
#similar to palindrome
#need to check for >2**31-1