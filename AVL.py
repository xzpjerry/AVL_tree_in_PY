class Node:
    def __init__(self, val):
        self.height = -1
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Avl:

    def __init__(self):
        self.root = None

    def __str__(self):
        q = [self.root] if self.root else []
        rslt = ''
        while len(q):
            curr = q.pop()
            rslt += "%d @ (%d)\n" % (curr.val, curr.height)
            if curr.left:
                q.insert(0, curr.left)
            if curr.right:
                q.insert(0, curr.right)
        return rslt

    def get_BF(self, node):
        if not node:
            return 0
        hl = node.left.height if node.left else 0
        hr = node.right.height if node.right else 0
        return hl - hr

    def rebalance(self, node):
        if not node:
            return None

        left_imbalanced = self.rebalance(node.left)
        right_imbalanced = self.rebalance(node.right)

        if left_imbalanced == None and right_imbalanced == None:
            hl = node.left.height if node.left else 0
            hr = node.right.height if node.right else 0
            if abs(hl - hr) > 1:
                print("Detect imbalance")
                return self._rebalance(node)
            else:
                return None
        return False

    def _rebalance(self, node):
        if node:
            # Left heavy
            if self.get_BF(node) > 0:
                if node.left:
                    # Right heavy
                    if self.get_BF(node.left) < 0:
                        node.left = self.single_right_rotate(node.left)
                node = self.single_left_rotate(node)

            # Right
            elif self.get_BF(node) < 0:
                if node.right:
                    # Left heavy
                    if self.get_BF(node.right) > 0:
                        node.right = self.single_left_rotate(node.right)
                node = self.single_right_rotate(node)
        return node

    def insert(self, val):
        self.root = self._insert(val, self.root)
        balance = self.rebalance(self.root)
        if balance:
            self.root = balance
        self.update_height(self.root)

    def _insert(self, val, node):
        if not node:
            node = Node(val)
            node.height = 0
        if val < node.val:
            node.left = self._insert(val, node.left)
        if val > node.val:
            node.right = self._insert(val, node.right)
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        return node

    def get_height(self, node):
        if not node:
            return -1
        return node.height

    def update_height(self, node):
        if not node:
            return -1
        node.height = max(self.update_height(node.left),
                          self.update_height(node.right)) + 1
        return node.height

    # Clockwise
    def single_left_rotate(self, node):
        if not node or not node.left:
            return
        # Will be the hub
        left_heavy_sub = node.left
        bak = left_heavy_sub.right
        left_heavy_sub.right = node
        node.left = bak
        return left_heavy_sub

    # Counter-clockwise
    def single_right_rotate(self, node):
        if not node or not node.left:
            return
        # Will be the hub
        right_heavy_sub = node.right
        bak = right_heavy_sub.left
        right_heavy_sub.left = node
        node.right = bak
        return right_heavy_sub

test = Avl()
'''
# Left rotation
print(test)
test.insert(10)
print(test)
test.insert(11)
print(test)
test.insert(8)
print(test)
test.insert(9)
print(test)
test.insert(7)
print(test)
test.insert(6)
print(test)
'''
print(test)
test.insert(7)
print(test)
test.insert(6)
print(test)
test.insert(9)
print(test)
test.insert(8)
print(test)
test.insert(10)
print(test)
test.insert(11)
print(test)
