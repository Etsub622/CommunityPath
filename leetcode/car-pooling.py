class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        psum=[0]*1001
        for k,f,t in trips:
            psum[f]+=k
            psum[t]-=k
     
        for i in range(1,1001):
            psum[i]+=psum[i-1]

        return max(psum)<=capacity                   

    
        