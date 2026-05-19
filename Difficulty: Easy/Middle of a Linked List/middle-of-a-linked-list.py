'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        if not head:
            return head
        count=0
        curr=head
        while curr:
           curr=curr.next
           count+=1
        mid = count//2
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr.data
