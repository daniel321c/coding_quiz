

def isSubTree(node1, node2):

    if(node1 is None):
        return True

    if(node2 is None):
        return False
    
    result = False

    if(node1.val == node2.val):
        result = result or (isSubTree(node1.left, node2.left) and isSubTree(node1.right, node2.right))
    
    result = result or isSubTree(node1, node2.left) or isSubTree(node1, node2.right)

    return result

# O(n, m) = O(n-1, m-1) +O(n, m-1) +O(n, ,m-1) 
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


n1 = Node(1, None, None)
n2 = Node(2, None, None)
n3 = Node(3, n1, n2)

s1 = Node(1, None, None)
s2 = Node(2, None, None)
s3 = Node(3, s1, s2)

print(isSubTree(n3, s2))

map = {1:3, 2:10}

l = list(map.items())

print(l[0][0])