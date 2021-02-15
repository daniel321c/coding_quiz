class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deserialize(str, node, start):

    if(str[start] != -1):
        new_node = Node(str[start])
        node.left = new_node
        start = deserialize(str, node.left, start+1)
    
    start += 1
    if(str[start] != -1):
        new_node = Node(str[start])
        node.right = new_node
        start = deserialize(str, node.right, start+1)
    
    return start

def helper(str):
    if(len(str) == 0):
        return None
    first_node = Node(str[0])
    deserialize(str, first_node, 1)
    return first_node


def serialize(node, arr):
    if(node is None):
        arr.append('-1')
    else:
        arr.append(str(node.val))
        serialize(node.left, arr)
        serialize(node.right, arr)
    return arr

node = helper([])

" ".join(serialize(node, []))


