import collections
class MaxQueue(object):

    def __init__(self):
        self.deque = collections.deque()
        self.sort_que = collections.deque()

    def max_value(self):
        """
        :rtype: int
        """
        if self.sort_que:
            return self.sort_que[0]
        else:
            return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.deque.append(value)
        while self.sort_que and self.sort_que[-1]<value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.deque:
            return -1
        result = self.deque.popleft()
        if result == self.sort_que[0]:
            self.sort_que.popleft()
        return result

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
