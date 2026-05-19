class Solution:
    def deleteNode(self, head, x):
        
        # delete first node
        if x == 1:
            return head.next
        
        curr = head
        
        # move to (x-1)th node
        for _ in range(x - 2):
            curr = curr.next
        
        # delete xth node
        curr.next = curr.next.next
        
        return head