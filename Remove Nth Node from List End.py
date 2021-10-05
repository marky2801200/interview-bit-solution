# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        c=0
        temp=A
        if B==1:
            pre=A
            curr=A.next
            while(curr):
                if curr.next==None:
                    pre.next=None
                    return A
                pre=curr
                curr=curr.next
        while(temp.next!=None):
            c+=1
            temp=temp.next
        c+=1
        if B>=c:
            A=A.next
            return A
        else:
            c=(c-B)+1
            curr=A.next
            pre=A
            z=2
            while(curr):
                if z==c:
                    if B==1:
                        pre.next=None
                    else:
                        pre.next=curr.next
                    break
                z+=1
                pre=curr
                curr=curr.next
            return A
