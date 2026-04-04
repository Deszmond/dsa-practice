class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Problem: is Anagram
        #Pattern: Hashmap
        #Time: O(s+t) -> O(n), for loops aren't nested and are sequential so is linear
        #Space O(s+t) -> O(n), created hashmaps which use space 


        #Check lengths of both strings
        if len(s) != len(t):
            return False

        #Create empty hashmaps to store values and counts
        checkS = {}
        checkT = {}

        #iterate through both strings and add to hashmap
        
        for char in s:
            if char in checkS:
                checkS[char] += 1

            elif char not in checkS:
                checkS[char] = 1

        for char2 in t:
            if char2 in checkT:
                checkT[char2] += 1

            elif char2 not in checkT:
                checkT[char2] = 1

        return checkS == checkT
