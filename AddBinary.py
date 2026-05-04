class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        total = 0
        i = len(a) - 1
        j = len(b) - 1      
        # The problem is askig to solve the sum of two binary as binary. 
        # I know I need to add the two inputs but how do I convert them into binary
        # First I add the two numbers together and then I can find the sum.
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                digit_a = int(a[i])
                i -= 1
            else:
                digit_a = 0
            if j >= 0:
                digit_b = int(b[j])
                j -= 1        
            else:
                digit_b =  0
            total = digit_a + digit_b + carry
            result.append(total % 2)
            carry = total // 2
        result.reverse()
        return ''.join(map(str, result))