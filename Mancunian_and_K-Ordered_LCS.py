from numpy import zeros
haha=list(map(int,input().split(" ")))
st1=list(map(int,input().split(" ")))
st2=list(map(int,input().split(" ")))
if haha[1]>haha[0]:
    for i in range(haha[1]-haha[0]):
        try:
            st2.append(int(input()))
        except:
            pass
lst1=len(st1)
lst2=len(st2)
dp=zeros((lst1+1,lst2+1),dtype=int)
for i,v in enumerate(st1):
    for j,_ in enumerate(st2):
        if v==_:
            dp[i+1][j+1]=1+dp[i][j]
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
ans=dp[-1][-1]+haha[-1]
small=[lst1 if lst1<lst2 else lst2][0]
if small<ans:
    print(small)
else:
    print(ans)
