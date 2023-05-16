class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
            }
        result = []
        while num > 0:
            if num >= 1000:
                num = num - 1000
                result.append(1000)
            elif num >= 500:
                num = num - 500
                result.append(500)
            elif num >= 100:
                num = num - 100
                result.append(100)
            elif num >= 50:
                num = num - 50
                result.append(50)
            elif num >= 10:
                num = num - 10
                result.append(10)
            elif num >= 5:
                num = num - 5
                result.append(5)
            elif num >= 1:
                num = num - 1
                result.append(1)
        print(result)
        for i in range(len(result)):
            result[i] = roman_dict[result[i]]
        result = "".join(result)
        result = result.replace("DCCCC","CM")
        result = result.replace("CCCC","CD")
        result = result.replace("LXXXX","XC") 
        result = result.replace("XXXX","XL")
        result = result.replace("VIIII","IX")
        result = result.replace("IIII","IV")
        return(result)
    



