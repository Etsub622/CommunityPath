class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1==0 or num2==0:
            return "0"
        result=[0]*(len(num1)+len(num2))
        
        for i in range(len(num1)-1,-1,-1):
            carry=0
            for j in range(len(num2)-1,-1,-1):

                temp_sum = result[i + j + 1] + carry + (int(num1[i]) * int(num2[j]))
                carry=temp_sum//10
                result[i+j+1]=temp_sum%10

            result[i]+=carry
        result=("".join(map(str,result))).lstrip("0")

        return result if result else "0"
                
        