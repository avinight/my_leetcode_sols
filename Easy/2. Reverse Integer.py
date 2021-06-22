class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = ''
        if str(x)[0] != '-':
            l = str(x)[::-1]
        else:
            l = '-' + str(x)[:0:-1]
        if (-(2**31)-1 < int(l) < (2**31)):
            return int(l)
        else:
            return 0
