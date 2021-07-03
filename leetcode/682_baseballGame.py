class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for record in ops:
            if record == "+": stack.append(stack[-1]+stack[-2])
            elif record == "D":stack.append(stack[-1]*2)
            elif record == "C":stack.pop()
            else:
                stack.append(int(record))
        return sum(stack)
