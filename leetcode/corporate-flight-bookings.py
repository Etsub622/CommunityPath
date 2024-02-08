class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        psum=[0]*(n+1)
        for f,l,s in bookings:
            psum[f-1]+=s
            psum[l]-=s
      
        ans=[0]*(n)
        acc=0
        for i in range(len(psum)-1):
            acc+=psum[i]
            ans[i]=acc

        return ans


        