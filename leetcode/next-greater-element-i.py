class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*len(nums2)
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=-1
            stack.append(nums2[i])
        output=[]
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            output.append(ans[idx])
        return output                  

        