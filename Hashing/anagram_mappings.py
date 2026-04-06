class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #Problem: Hashing for direct address lookup
        # Thought Process: Store index of nums2 and map into res array
        #Time Complexity: Loop both arrays which is O(2n) -> O(n)
        #Space Complexity: O(n), 'store' & 'res' both hold n elements

        store = {}
        res = [0]*len(nums1)

        for i, num in enumerate(nums2):
            store[num]=i

        for i, num in enumerate(nums1):
            res[i] = store[num]

        return res
