class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        # Pattern: Hashmap
        # Key Idea:Cchar count as key via hashmap, word themselves are respective values
        # Time: O(n*m)
        # Space: O(n*m)

        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1

            key = tuple(count)
            res[key].append(word)

        return list(res.values())