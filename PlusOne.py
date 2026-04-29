class Solution(object):
    # Problem: Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
    # Key idea: start from the last digit and move left, handling carry when needed.
    # Core Technique: Right-to-left traversal with early exit. iterate from the last index backwards. At each step, either absorb the carry and stop.
        # Or set the digit to 0 and continue. if you exhaust the array, prepend a 1.

    # Time Complexity: O(n) - Worst case: you iterate through the entire array.
        # For most inputs you touch one element but fo input like 999 with n digits, you vist every element. 
    # Space Complexity: O(1) - No additional space needed, just modifying the input array.

    # One thing moving through the array -> Just a loop variable(i).
    # two things at different positions doing work together -> Left and Right pointer.

    # Resuable Patterns: 
    # Right to left traversal -> When an operation at position i depends on position i+1 (or carry propagates right->left), 
     # Iterate backwards. Common in: addition, string parsing, palindrome checks.
    # Early exit -> Always look for an exit condition inside the loop. As soon as carry is resolved, return.
    # Egde case: Overflow past array bounds -> If the loop finishes without returning, the carry outlasted the array.
     # Handle with a prepend, Same patterns appears in: Biginteger addition, String concatenation.
    # Index-based vs value-based iteration -> If you need to mutate the array, you need the index. for i in range(...) gives you write access.
     # for x in arr gives you a read-only copy of each value.
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Loop through the array backwards. right to left. 
        # if normal loop would be range(len(digits)), it would be left to right.
        for i in range(len(digits)-1, -1, -1):
            # if the digit is less than 9
            if digits[i] < 9:
                # increment the digit by 1
                digits[i] += 1
                # return the digits
                return digits
            # if the digit is 9
            # set the digit to 0
            digits[i] = 0
        # if the loop finishes without returning, the carry outlasted the array.
        # prepend a 1.
        return [1] + digits

# Does the result have the same shape as the input?
    #Yes → modify in place, no new array needed
    #No (different size, different structure) → you need a new array