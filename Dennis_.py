#check whether unit digit of the cube is the same as the number input
# from re import L


# n=int(input())
# ans=""
# if(n>10000):
#     ans="Wrong Input"
# elif((n*n*n)%10==n):
#     ans="True"
# else:
#     ans="False"
# print(ans)
#Dennis was solving a puzzle. The puzzle was to verify a number whose cube ends with the number itself. Help Dennis to find the solution to the puzzle and write the code accordingly. If the input is greater than 10000, print "Wrong Input".

n=int(input())
if(n>10000):
    print("Wrong Input")
else:
    p=n*n*n
    l1=len(str(n))
    l2=len(str(p))
    s1=str(n)
    s2=str(p)

    l=l2-l1
    s=s2[l:]
    if(s==s1):
        print("True")
    else:
        print("False")