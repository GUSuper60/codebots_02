from itertools import accumulate
t=int(input())
for _ in range(t):
    
    walker=int(input())
    distance=list(map(int,input().split(" ")))
    a=max(distance)+1
    hashtab=[0]*a
    flag=True
    
    for i in distance:
        hashtab[i]+=1
      
    hashtab=list(accumulate(hashtab))
    
    for i,v in enumerate(hashtab):
        blah=(i+1)-(i//7)
        if v>=blah:
            print('Goodbye Rick')
            print(blah-1)
            flag=False
            break
    if flag==True:
        print('Rick now go and save Carl and Judas')
