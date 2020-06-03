import sys
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.resultmin = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.resultmin.append(x)
        else:
            if x<self.resultmin[-1]:
                self.resultmin.append(x)
            else:
                self.resultmin.append(self.resultmin[-1])
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.resultmin.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.resultmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()