"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_copies = {None: None}
        
        temp = head
        while temp:
            node_copies[temp] = Node(temp.val, None, None)
            temp = temp.next
            
        curr = head
        while curr:
            copy = node_copies[curr]
            copy.next = node_copies[curr.next]
            copy.random = node_copies[curr.random]
            curr = curr.next
        
        return node_copies[head]
