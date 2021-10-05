from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, l):
        d=Counter(l)
        for p in d.keys():
            if d[p]==1:
                return p
