class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        j = 1
        number1 = 0
        number2 = 0
        for i in num1:
            number1 += int(i)*j
            j = j*10
        j=1
        for i in num2:
            number2 += int(i)*j
            j = j*10
        result = str(number1*number2)
        return(result)
