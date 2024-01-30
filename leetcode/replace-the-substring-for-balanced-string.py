class Solution:
    def balancedString(self, s: str) -> int:
        count=Counter(s)
    
        extra=''
        for c in count:
            if count[c]>len(s)//4:
                extra+=(count[c]-len(s)//4)*c
        if not extra:
           return 0
        
        extraCount=Counter(extra)
        l,ans=0,float('inf')
        freq=Counter()
        for r,char in enumerate(s):
            freq[char]+=1

            while extraCount-freq==Counter():
                ans=min(ans,r-l+1)
                freq[s[l]]-=1
                l+=1
        return ans        
        







    # dic=defaultdict(list)
    # for i in range(len(s)):
    #     dic[s[i]].append(i)
    # print(dic) 
       

    # excess=[]
    # size=0
    # for i,val in dic.items():
    #     if len(val)>len(s)/4:
    #         excess.extend(val)
    #         size+=len(val)-len(excess)
    # excess.sort()
    # print(excess)
    # diff=float('inf')
    # for i in range(len(excess)):
    #     winSize=excess[i:i+size]
        
    #     l=0
    #     while winSize:
    #         diff+=min(diff,abs(winSize[i]-winSize[i]))
    #         l+=1
    # return diff if diff!=float('inf') else 0





        
        # dic=defaultdict(list)
        # for i in range(len(s)):
        #     dic[s[i]].append(i)
        # print(dic) 
           

        # excess=[]
        # size=0
        # for i,val in dic.items():
        #     if len(val)>len(s)/4:
        #         excess.extend(val)
        #         size+=len(val)-len(excess)
        # excess.sort()
        # print(excess)
        # diff=float('inf')
        # for i in range(len(excess)):
        #     winSize=excess[i:i+size]
            
        #     l=0
        #     while winSize:
        #         diff+=min(diff,abs(winSize[i]-winSize[i]))
        #         l+=1
        # return diff if diff!=float('inf') else 0        





