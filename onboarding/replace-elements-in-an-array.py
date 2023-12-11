class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # dic = {}
        # for item in nums:
        #     dic[item] = item

        # for old,new in operations:
        #     nums[dic[old]]=new
            

        # output=[]
        # for value in my_dict.values():
        #     output.append(value)
        # return output    
        dic=defaultdict(int)
        for i ,num in enumerate(nums):
            dic[num]=i
        for old,new in operations:
            nums[dic[old]]=new
            dic[new]=dic[old]
                
        return nums        

