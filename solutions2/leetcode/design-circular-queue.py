class MyCircularQueue(object):

    def __init__(self, k):
        self.size  = k
        self.queue = []

    def enQueue(self, value):
        if not self.isFull():
            self.queue.append(value)
            return True
        return False
    def deQueue(self):
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        return False


    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[0]


    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[-1]


    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()