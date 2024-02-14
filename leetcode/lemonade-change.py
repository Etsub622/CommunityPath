class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic=defaultdict(int)
    
        for i in range(len(bills)):
            if bills[i]==5:
                dic[5]+=1
            elif bills[i]==10:
                if 5 not in dic:
                    return False
                else:
                    dic[5]-=1
                    dic[10]+=1
        
            else:
               
                if (dic[10]>=1 and dic[5]>=1):
                    dic[10]-=1
                    dic[5]-=1
                
                elif  dic[5]>=3:
                    dic[5]-=3 
                
                else:
                    return False
        return True            

                        
                            
        