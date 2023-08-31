class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = []
        result = ""
        for i in range(len(s)-1,-1,-1):
            word=""
            if s[i] == " " or i == 0:
                if i == 0 or i == len(s)-1: j=i
                else: j=i+1
                if i == 0 and s[i] == ' ':
                    j=i+1
                while s[j] != " ":
                    if s[j] != " ": word = word + s[j]
                    if j==len(s)-1:
                        break
                    j+=1
                list_of_words.append(word)
        for i in list_of_words:
            if i != "":
                result = result + i + ' '
        result = result[:-1]
        return(result)