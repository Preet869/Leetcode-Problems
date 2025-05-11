# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution(object):
    def romanToInt(self, s):
        # 1. Create a dictionary for Roman numeral values
        numerals = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}   
        # 2. Initialize total to 0
        total = 0
        # 3. Loop through each character in the string (by index)
        for i in range(len(s)):
            # 4. Get the value of the current numeral
            current_value = numerals[s[i]]
            # 5. Check if there's a next numeral AND if the current one is less than the next one
            if i + 1 < len(s) and current_value < numerals[s[i + 1]]:
                # 6. If so, subtract current value from total
                total -= current_value
            else:
                # 7. Otherwise, add current value to total
                total += current_value   
        # 8. Return the total after the loop
        return total