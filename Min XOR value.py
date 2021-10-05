class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, l):
        l.sort()
        ans=float('inf')
        for i in range(1,len(l)):
            a=l[i]^l[i-1]
            ans=min(ans,a)
        return ans
