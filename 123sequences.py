#AdemHosama
t=int(input())
h=list(map(int,input().split()))
a=h.count(1)
b=h.count(2)
c=h.count(3)
d=max(a,b,c)
print(len(h)-d)
