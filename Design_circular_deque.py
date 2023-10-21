class MyCircularDeque(object):
    def __init__(self, k):
        self.list = []
        self.maxLength = k

    def insertFront(self, value):
        if not self.isFull():
            self.list.insert(0, value)
            return True
        return False

    def insertLast(self, value):
        if not self.isFull():
            self.list.append(value)
            return True
        return False

    def deleteFront(self):
        if not self.isEmpty():
            self.list.pop(0)
            return True
        return False

    def deleteLast(self):
        if not self.isEmpty():
            self.list.pop()
            return True
        return False

    def getFront(self):
        if not self.isEmpty():
            return self.list[0]
        return -1

    def getRear(self):
        if not self.isEmpty():
            return self.list[-1]
        return -1

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return self.maxLength == len(self.list)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
