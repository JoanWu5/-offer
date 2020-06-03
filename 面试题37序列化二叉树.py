import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')   
        return '['+','.join(result)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        result = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(result[0]))
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if result[i]!='null':
                node.left = TreeNode(int(result[i]))
                queue.append(node.left)
            i+=1
            if result[i]!='null':
                node.right = TreeNode(int(result[i]))
                queue.append(node.right)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.deserialize("[1,2,3,null,null,4,5]"))