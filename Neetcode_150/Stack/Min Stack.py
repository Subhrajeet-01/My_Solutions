class MinStack(object):

    def __init__(self):
        self.array = []
        
    def push(self, val):
        self.array.append(val)
        
    def pop(self):
        self.array.pop(-1)
        
    def top(self):
        x = self.array[-1]
        return x
        
    def getMin(self):
        return min(self.array)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
