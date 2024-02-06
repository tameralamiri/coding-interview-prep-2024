# Solving the "Repeated DNA Sequences" Challenge
# Challenge Description:
# Given a string representing a DNA sequence, find all the 10-letter-long sequences 
# (substrings) that occur more than once in the DNA molecule.

# Example:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# Solution:
# The solution is based on the sliding window technique. We use a dictionary to store
# the substrings and their counts. We iterate over the string and add the substrings
# to the dictionary. If the substring is already in the dictionary, we increment its
# count. Finally, we return all the substrings that have a count greater than 1.

# Time Complexity: O(n)
# Space Complexity: O(n)
def find_repeated_dna_sequences(s):
    if len(s) < 10:
        return []
    
    substrings = {}
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    return [substring for substring in substrings if substrings[substring] > 1]

# Optimized Solution:
# We can optimize the solution by using a set instead of a dictionary. We add the
# substrings to the set and if the substring is already in the set, we add it to the
# result set. Finally, we return the result set as a list.
# This optimzation will reduce the space complexity from O(n) to O(n/10) which is
# equivalent to O(n).

# Time Complexity: O(n)
# Space Complexity: O(n)
def find_repeated_dna_sequences_optimized(s):
    if len(s) < 10:
        return []
    
    substrings = set()
    result = set()
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in substrings:
            result.add(substring)
        else:
            substrings.add(substring)
    
    return list(result)

# Tests:
print(find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # ["AAAAACCCCC", "CCCCCAAAAA"]
print(find_repeated_dna_sequences("AAAAAAAAAAAAA")) # ["AAAAAAAAAA"]