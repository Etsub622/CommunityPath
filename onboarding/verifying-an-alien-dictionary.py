class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDic = {}
        for i in range(len(order)):
            orderDic[order[i]] = i
    
        def toBeSorted(word):
            rightOrder = []
            for char in word:
                rightOrder.append(orderDic[char])
            return rightOrder

        sortedOrder = sorted(words, key=toBeSorted)
        return sortedOrder == words

     
      
         

