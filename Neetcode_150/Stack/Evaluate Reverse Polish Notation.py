class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for ele in tokens:
            if ele not in ["+","-","*","/"]:
                stack.append(int(ele))
            else:
                a = stack.pop()
                b = stack.pop()
                if ele == "+":
                    ans = (a)+(b)
                elif ele == "-":
                    ans = (b) - (a)
                elif ele == "*":
                    ans = (b) * (a)
                else:
                    ans = int(float(b)/(a))  
                stack.append(ans)
        return stack[0]
                      
