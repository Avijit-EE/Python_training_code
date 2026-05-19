'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def insertPos(self, head, pos, value):
        new_node = Node(value)
        
        if(pos == 1):
            new_node.next = head
            return new_node
        curr=head
        for i in range(1, pos - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        
        return head