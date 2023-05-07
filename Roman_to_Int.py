class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        result = 0
        integer_values = []
        for i in s:
            integer_values.append(roman_dict[i])
        for i in range(len(integer_values)-1):
                if integer_values[i] < integer_values[i+1]:
                    integer_values[i+1] = integer_values[i+1] - integer_values[i]
                    integer_values[i] = 0
        result = sum(integer_values)
        return(result)


