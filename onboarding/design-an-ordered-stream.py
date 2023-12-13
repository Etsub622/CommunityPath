class OrderedStream:

    def __init__(self, n: int):
        self.array=[0]*(n+1)
        self.l=1
 
    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey]=value

        ans=[]
        while self.l<len(self.array) and self.array[self.l]!=0:
            ans.append(self.array[self.l])
            self.l+=1
        return ans    
         

        
                  






        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)