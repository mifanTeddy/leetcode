class Solution:
    def numDecodings(self, s: str) -> int:
        # w tells the number of ways
        # v tells the previous number of ways
        # d is the current digit
        # p is the previous digit
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w