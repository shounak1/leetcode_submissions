class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos_limit = 2**31 - 1
        print ("Postive limit : ", pos_limit)
        
        neg_limit = -1 * (2**31)
        print ("Negative limit : ", neg_limit)
        
        n = len(str(x)) - 1
        negative = False
        if (x < 0):
            negative = True
            x = -1 * x
            n = n - 1
        new_number = 0
        while (1):
            remainder = x / 10
            quotient = x % 10
            print ("Remainder : ", remainder)
            print ("Quotient : ", quotient)  
            x = remainder
            new_number = new_number + quotient * (10**n)
            print ("New number : ", new_number)
            n = n - 1
            if (n == -1):
                break
        if new_number > pos_limit or new_number < neg_limit:
            return 0
        if negative:
            return -1 * new_number
        else:
            return new_number
