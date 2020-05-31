class CQueue(object):
    # def __init__(self):
    #     self.stack = []

    # def appendTail(self, value):
    #     """
    #     :type value: int
    #     :rtype: None
    #     """
    #     self.stack.append(value)

    # def deleteHead(self):
    #     """
    #     :rtype: int
    #     """
    #     if self.stack:
    #         return self.stack.pop(0)
    #     else:
    #         return -1

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stackin.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stackout:
            return self.stackout.pop()
        elif not self.stackin:
            return -1
        else:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()

obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())