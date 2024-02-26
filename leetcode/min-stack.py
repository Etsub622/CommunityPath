class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self, val: int) -> None:

        self.stack.append(val)
        if self.minStack==[]:
            self.minStack.append(val)
        else:
            # if val < self.minStack[-1]:
                
            #     self.minStack.append(val)
            # else:
            #     pass    
            self.minStack.append(min(val,self.minStack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1    

        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return -1    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()