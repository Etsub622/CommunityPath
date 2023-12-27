class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1=set(nums1)
        num2=set(nums2)


        output=[]
        for i in num1:
            if i in num2:
                n=nums1.count(i)
                m=nums2.count(i)
                added=min(m,n)


                output.extend([i]*added)
        return output        






        