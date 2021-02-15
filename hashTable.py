class HashTable:
    def __init__(self):
        self.size = 2
        self.table = [[] for _ in range(self.size)]
        self.cap = 0

    def put(self, key, val):
        ret = self.put_helper(key, val, self.table)
        # may have collision when insert new key
        if (ret):
            self.cap += 1
            if (self.cap > self.size):
                self.rehash()

    def get(self, key):
        node = self.get_helper(key, self.table)
        if (node is not None):
            return node.val

    def remove(self, key):
        node = self.get_helper(key, self.table)
        if (node is not None):
            pos = hash(key) % self.size
            self.table[pos].remove(node)
            self.cap -= 1

    def rehash(self):
        newtable = [[] for _ in range(2 * self.size)]

        for list in self.table:
            for node in list:
                self.put_helper(node.key, node.val, newtable)
        self.table = newtable
        self.size *= 2

    def get_helper(self, key, table):
        pos = hash(key) % len(table)
        for node in table[pos]:
            if (node.key == key):
                return node

    def put_helper(self, key, val, table):

        node = self.get_helper(key, table)
        if (node is not None):
            node.val = val
            return False
        else:
            node = Node(key, val)
            pos = hash(key) % len(table)
            table[pos].append(node)
            return True
