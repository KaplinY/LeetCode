s = "loveleetcode"
letter = {}
for i in s:
    if i in letter:
        letter[i] = 2
    else:
        letter[i] = 1
for i in letter:
    if letter[i] == 1:
        result = i
        break
for i in range(len(s)):
    if s[i] == result:
        print(i)
