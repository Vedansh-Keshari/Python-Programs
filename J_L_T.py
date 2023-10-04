T=int(input())
for i in range(T):
    s=input()
    s=s.split()
    X=int(s[0])
    Y=int(s[1])
    ans=X//Y
    print(ans)