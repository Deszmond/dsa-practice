class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Pattern: Scan right-to-left, carry the best so far.
        # Time: O(n)
        # Space: O(1)

        #Going to traverse the array backwards and comapare maximum from R -> L

        rightMax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr
