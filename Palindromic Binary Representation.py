class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, a):
        if a==1:
            return 1
        a=a-1
        q=['11']
        while len(q)!=0:
            c=q.pop(0)
            a-=1
            if a==0:
                return int(c,2)
            l=len(c)
            if l%2==0:
                q.append(c[:int(l/2)]+'0'+c[int(l/2):])
                q.append(c[:int(l/2)]+'1'+c[int(l/2):])
            else:
                mid=c[int(l/2)]
                q.append(c[:int(l/2)]+mid+c[int(l/2):])
        return 0
