class Solution:
    def longestUniqueSubstring(self, s):
        max_len = 0

        for i in range(len(s)):

            visited = set()
            length = 0

            for j in range(i, len(s)):

                if s[j] in visited:
                    break
                else:
                    visited.add(s[j])
                    length += 1

                max_len = max(max_len, length)

        return max_len