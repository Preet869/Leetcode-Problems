"""
We check if there are still digits left. If yes, we take the current character, 
convert it to an integer so we can perform arithmetic, and move the pointer left. 
If not, we use 0 to handle unequal lengths.

BIG O Notation:
The time complexity is O(n) because we iterate through each digit of the input strings at most once. 
Even though there are two strings, we process them in a single loop using two pointers, 
so the total work scales linearly with the length of the longer string.”

"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        total = 0
        i = len(num1) - 1
        j = len(num2) - 1
        # The problem requires us to find the sum of two strings.
        # The carry happens when the string is 10. 
        # Since we are looking for the carry we will start from right -> left.
        # I need to apply the same logic 
        # Create the while loop:
        while i >= 0 or j >= 0 or carry:
            # Check if i is euqal or less then 0
            if i >= 0:
                digital_1 = int(num1[i])
                i -= 1
            else:
                digital_1 = 0
            if j >= 0:
                digital_2 = int(num2[j])
                j -= 1
            else:
                digital_2 = 0
            # I need to add the total and look for the carry
            total = digital_1 + digital_2 + carry
            result.append(total % 10)
            carry = total // 10
        result.reverse()
        return ''.join(map(str, result))

