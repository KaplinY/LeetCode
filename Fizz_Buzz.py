class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=list(range(1,n+1))
        for i in range(len(answer)):
            if answer[i]%3 == 0 and answer[i]%5 == 0:
                answer[i] = "FizzBuzz"
                continue
            if answer[i]%3 == 0:
                answer[i] = "Fizz"
                continue
            elif answer[i]%5 == 0:
                answer[i] = "Buzz"
                continue
            answer[i] = str(answer[i])
        return (answer)w


