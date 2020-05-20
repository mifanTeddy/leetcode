class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz, ret = zip(*strs), ""
        for c in sz:
            if len(set(c)) > 1:
                break
            ret += c[0]
        return ret
