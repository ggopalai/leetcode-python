class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """
        Finds the length of the longest valid substring which does not contain any of the forbidden words.
        """
        res = left = 0
        forbidden = set(forbidden)

        # O(N)
        for i in range(len(word)):
            # O(10)
            for j in range(max(left, i - 9), i + 1):
                if word[j:i+1] in forbidden:
                    left = j + 1
            res = max(res, i - left + 1)
        
        return res