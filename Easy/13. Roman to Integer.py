class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rns = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        out = 0
        for i in range(0, len(s), 1):
            if i+1 < len(s) and rns[s[i]] < rns[s[i+1]]:
                out -= rns[s[i]]
            else:
                out += rns[s[i]]
        return out
