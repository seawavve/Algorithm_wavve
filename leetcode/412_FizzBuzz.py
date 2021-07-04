class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for idx,val in enumerate(range(n),start=1):
            if (idx%3==0) and (idx%5==0):
                res.append('FizzBuzz')
            elif (idx%3==0):
                res.append('Fizz')
            elif (idx%5==0):
                res.append('Buzz')
            else:
                res.append(str(idx))
        return res
        
