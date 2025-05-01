#AdemHosam
s = input()
t = input()

i = len(s) - 1
j = len(t) - 1

while i >= 0 and j >= 0 and s[i] == t[j]:
    i -= 1
    j -= 1

print(i + j + 2)
