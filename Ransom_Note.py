class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = 0
        for i in range(len(ransomNote)):
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j]:
                    counter = counter + 1
                    magazine = magazine.replace(magazine[j],'',1)
                    break
        if counter == len(ransomNote):
            return True
        else:
            return False

