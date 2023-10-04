def magic_square(n):
    n=int(n)
    ms=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        ms.append(l)
        
    i = n//2
    j = n-1
    
    num=n*n
    count = 1
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i==-1):
                i=n-1
        if(ms[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            ms[i][j]=count
            count+=1
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(ms[i][j],end=" ")
        print()
        
    print("The sum of each row/column/diagonal is "+str(n*(n**2 + 1)//2))
        
magic_square(3)
