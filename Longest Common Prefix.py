# Problem: 14. Longest Common Prefix
  # Write a function to find the longest common prefix string amongst an array of strings.
  # If there is no common prefix, return an empty string "".

# Time Complexity:
    # O(S) where S is the sum of all characters in all strings.
    # Worst-case: compare every character in all strings.


# Logic 
    # Correct Logic:
    # Assume the first string is the initial prefix.
    # Loop through the rest of the strings.
    # Trim the prefix until it matches the start of each string.
    # If at any point the prefix becomes empty, return "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first word as the prefix
        prefix = strs[0]

        for word in strs[1:]:
            # Keep trimming the prefix until it matches the current word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
