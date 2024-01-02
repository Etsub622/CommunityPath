class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        
        output = 0
        current=0
        for i in range(len(processorTime)):
            current=(processorTime[i] + tasks[i*4])
            output = max(output,current )
        
        return output 

       


            


             



        