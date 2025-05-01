
#AdemHosama
t=int(input())
s=list(map(int,input().split()))
non_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]

cal = []
for i in range(20):
    if i % 4 == 3:
        cal += leap
    else:
        cal += non_leap

f=False 
for i in range(len(cal)-t+1):
    if cal[i:i+t] == s:
        f= True
        break
if f:
    print("YES")
else:
    print("NO")
