class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzList = []
        for i in range(n):
            div3 = True if ((i+1) % 3 == 0) else False
            div5 = True if ((i+1) % 5 == 0) else False
            if div3 and div5:
                fizzList.append("FizzBuzz")
            elif div3:
                fizzList.append("Fizz")
            elif div5:
                fizzList.append("Buzz")
            else:
                fizzList.append(str(i+1))
        return fizzList