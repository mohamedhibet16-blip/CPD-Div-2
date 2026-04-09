class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]  # take first string

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last character

                if prefix == "":
                    return ""

        return prefix
