

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = {}
        max_len = 0
        start = 0

        for index, char in enumerate(s):
            if char in exist and start <= exist[char]:
                start = exist[char] + 1
            else:
                max_len = max(max_len, index - start + 1)

            exist[char] = index

        return max_len
