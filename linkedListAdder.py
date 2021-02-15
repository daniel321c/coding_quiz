class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def construct(s):
    node = None
    for c in s:
        node = Node(int(c), node)
    
    return node

def printNode(node):

    while(node is not None):
        print(node.val)
        node = node.next


def adder(node1, node2):

    carry  = 0
    dummy = Node(-1, None)

    prev = dummy
    while(node1 is not None or node2 is not None):
        val1 = 0 
        val2 = 0
        if(node1 is not None):
            val1 = node1.val
            node1 = node1.next
        if(node2 is not None):
            val2 = node2.val
            node2 = node2.next

        val = (val1+val2+carry)%10
        
        carry = int((val1+val2+carry)/10)

        prev.next = Node(val, None)
        prev = prev.next

    return dummy.next

def reverse(node):
    if(node is None):
        return None
    first = None
    sec = node
    third = None

    while(sec is not None):
        third = sec.next
        sec.next = first
        first = sec
        sec = third
    
    return first
        



n = construct('23')
a = construct('56')
printNode(adder(n, a))
