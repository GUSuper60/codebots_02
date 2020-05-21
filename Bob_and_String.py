t=int(input())
for _ in range(t):
    a=input()
    b=input()
    ans=0
    for i in b:
        c=a.find(i)
        if c>=0:
            a=a[:c]+a[c+1:]
        else:
            ans+=-1*c
    print(len(a)+ans)
