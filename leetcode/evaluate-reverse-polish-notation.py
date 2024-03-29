class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack=[]
        operators={"+":operator.add,
                    "-":operator.sub,
                    "*":operator.mul,
                    "/":operator.truediv}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if stack:
                    num2=stack.pop()
                    num1=stack.pop()
                    result=operators[i](num1,num2)
                    stack.append(int(result))
        return stack[0]       