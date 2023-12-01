class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)-1
        output=sum(salary)-(salary[0]+salary[n])
        return output/(n-1)   
        