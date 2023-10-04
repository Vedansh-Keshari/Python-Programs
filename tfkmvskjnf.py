# def suum(n):
#     summ=0
#     x=n
#     while(x!=0):
#         summ=x%10
#         x=x/10
#     return summ
    
# suum(34)
# n=int(input())
# s=suum(n)
# while True:
#     if(s<=9):
#         break
#     else:
#         s=suum(s)
        
# print(s)

# 

# def getSum(n):
    
#     sum = 0
#     for digit in str(n): 
#       sum += int(digit)      
#     return sum
   
# n = 123456
# print(getSum(n))

# x=5
# while (x<15):
#   print(x**2)
#   x+=3

# i=2
# for x in range(i):
#   x+=1
#   print(x)
# print(x)

# for x in range (1,5):
#   for y in range (1,x+1):
#     print(y,end="")
#   print()

# for x in range (4,0,-1):
#   for y in range (1,x+1):
#     print("*",end="")
#   print()
"""
import math
n=int(input("Enter any number : "))
print("The square root of",n,"is",math.sqrt(n))

num_str = input("Input an integer (-1 terminates) : ")
num_int=int(num_str)
prime=0
composite=0
if(num_int%2==0):
  composite+=1
else:
  prime+=1
while (num_int!=0):
  num_str = input("Input an integer (-1 terminates) : ")
  num_int=int(num_str) 
  if((num_int==-1)):
    break
  elif ((num_int)%2==0):
    prime+= 1
    print(prime)
  else:
    composite +=1
    print(composite)

print("Number of prime numbers : ",prime)
print("Number of composite numbers : ",composite)
"""
# n=int(input("Enter number of days : "))
# sum=0
# if(n<=5):
#   sum=n*2
# elif(n<=10):
#   sum=5*2+(n-5)*3
# elif(n<=15):
#   sum=5*2+5*3+(n-10)*4
# else:
#   sum=5*2+5*3+5*4+(n-15)*5
# print("Amount payable : Rs.",sum)

# age=int(input("Enter age : "))
# sex=input("Enter sex (M/F): ")
# wages=0
# if(age>=18 and age<30):
#   if(sex[0]=='M' or sex[0]=='m'):
#     wages=700
#   elif(sex[0]=='F' or sex[0]=='f'):
#     wages=750
#   else:
#     wages=0
# elif(age>=30 and age<=40):
#   if(sex[0]=='M' or sex[0]=='m'):
#     wages=800
#   elif(sex[0]=='F' or sex[0]=='f'):
#     wages=850
#   else:
#     wages=0
# else:
#   wages=0
# if(wages==0):
#   print("Invalid Input")
# else:
#   print("Wage of the worker is : Rs.",wages)

# n=int(input("Enter any number : "))
# x=n
# i=2
# prime=True
# while(i<n):
#   if(x%i==0):
#     prime=False
#     break
#   i+=1
# if(prime):
#   print(n,"is a Prime Number")
# else:
#   print(n,"is a Composite Number")

# n=input("Enter any number : ")
# sum=0
# for i in (n):
#   sum=sum+int(i)**3
#   print(sum)
# if(sum==int(n)):
#   print(n,"is an Armstrong Number")
# else:
#   print(n,"is not an Armstrong Number")

# n=int(input("Enter any number : "))
# sum=0
# for i in range(1,n+1):
#   sum=sum+(i**3)
# print("Sum of the series uptil term "+str(n)+" is : "+str(sum))

# n1=int(input("Enter first number  : "))
# n2=int(input("Enter second number : "))
# sum_odd=0
# sum_even=0

# for i in range(n1,n2+1):
#   if(i%2==1):
#     sum_odd+=i
#   else:
#     sum_even+=i
# print("Sum of odd  numbers from",n1,"to",n2,"is : ",sum_odd)
# print("Sum of even numbers from",n1,"to",n2,"is : ",sum_even)

# n=int(input("Enter any number : "))
# i=1
# while(i<=10):
#     t=n*i
#     print(n,"x",i,"=",t)
#     i=i+1

# n=int(input("Enter any Number : "))
# r = 0
# while(n > 0):
#     R = n % 10
#     r = (r *10) + R
#     n = n // 10

# print("Reverse of the entered number is : ",r)


# list = [10, 21, 4, 45, 66, 93, 33, 22]
# for num in list:
#   if (num%2!=0):
#     print(num,end=" ")

# s='PYTHON'
# for x in s:
#   print(x)

# num=int(input("Enter any number : ")) 
# if (num%5==0):
#   print("Hello") 
# else: 
#   print("Bye") 

 
# num=int(input("Enter any number"))  
# ld=num%10
# if ld%3==0:  
#   print("Last digit of number is divisible by 3 ")  
# else:  
#   print("Last digit of number is not divisible by 3 ") 

# amt=0  
# nu=int(input("Enter number of electric unit"))  
# if nu<=100:  
#   amt=0  
# if nu>100 and nu<=200:  
#   amt=(nu-100)*5  
# if nu>200:  
#   amt=500+(nu-200)*10  
# print("Amount to pay :",amt)

# per = int(input("Enter marks : "))  
# if per > 90:  
#   print("Grade is A")  
# if per > 80 and per <=90:  
#   print("Grade is B")  
# if per >=60 and per <= 80:  
#   print("Grade is C")  
# if per < 60:  
#   print("Grade is D") 

# city = input("Enter name of the city : ") 
# if city.lower()=="delhi": 
#   print("Monument name is : Red Fort") 
# elif city.lower()=="agra": 
#   print("Monument name is : Taj Mahal") 
# elif city.lower()=="jaipur": 
#   print("Monument name is : Jal Mahal") 
# else: 
#   print("Enter correct name of city")

# num=int(input("Enter any number : "))
# p=1  
# while(num):  
#   r=num%10  
#   p=p*r  
#   num=num//10  
# print("Product of digits is",p) 

# num=int(input("Enter any number : "))  
# f=1  
# for i in range(1,num+1):
#   f=f*i
# print("Factorial of",num,"is",f) 


# num=int(input("Enter any number : "))  
# f=0  
# if num==1 or num==0:  
#   f=1  
# for i in range(2,num):  
#   if num%i==0:  
#     f=1  
# if f==1:  
#   print("Number is not prime")  
# else:  
#   print("Number is prime")

# n1=int(input("Enter first number  : "))
# n2=int(input("Enter second number : "))
# def prime(x):
#   f=0
#   for i in range(2,x):
#     if x%i==0:
#       f+=1
#   if f==0:
#     print(x)

# if n1<n2:
#   for j in range(n1,n2+1):
#     prime(j)

# elif n2<n1:
#   n1,n2=n2,n1   
#   for j in range(n1,n2+1):
#     prime(j)

# num = 0
# tot = 0.0
# while True:
#     number = input("Enter a number : ")
#     if number == '0':
#         break
#     num = num+1
#     tot = tot + num
# print("Sum : ",tot)
# print("Average : ",(tot/num))

# x=input("Enter the string : ")
# found=False 
# for i in x:
#   if (i=='A' or i=='a'): 
#     found=True
#   else: 
#     found=False

# if (found==True): 
#   print("Letter 'A' was found") 
# else: 
#   print("Letter 'A' not found")

# num=int(input("Enter any number : ")) 
# s=0
# for i in range(1,num): 
#   if num%i==0: 
#     s=s+i 
# if num==s: 
#   print("Number is perfect") 
# else: 
#   print("Number is not perfect")

# def primn(num): 
#   f=0 
#   if num==1 or num==0: 
#     f=1 
#   for i in range(2,num):
#     if num%i==0: 
#       f=1 
#   if f==1: 
#     return 'n' 
#   else: 
#     return 'y' 
# num=int(input("Enter number : ")) 
# for i in range(num): 
#   r=primn(i) 
#   if r=='y': 
#     print(i)

# # Num= 105 
# # while Num>=7: 
# #   print(Num,end=",") 
# #   Num=Num-7 

# # num1 = int(input("Enter first number : ")) 
# # num2 = int(input("Enter second number : ")) 
# # sum=0
# # for x in range(num1,num2+1):
# #   if(x%2==0):
# #     sum+=x
# # print(sum)

# def mergeSort(ar):
#     if len(ar)>1:
#         mid = len(ar)//2
#         L = ar[:mid]
#         R = ar[mid:]
#         mergeSort(L)
#         mergeSort(R)  
#         i=j=k=0
#         while i<len(L) and j<len(R):
#             if L[i] < R[j]:
#                 ar[k] = L[i]
#                 i += 1
#             else:
#                 ar[k] = R[j]
#                 j += 1
#             k += 1
#             while i<len(L):
#                 ar[k] = L[i]
#                 i += 1
#                 k += 1
#             while j<len(R):
#                 ar[k] = R[j]
#                 j += 1
#                 k += 1

# def printList(ar):
#     for i in range(len(ar)):
#         print(ar[i], end=" ")
#     print()

# ar = [3,6,2,8,9,23,56,12]
# print("Given array is", end="\n")
# printList(ar)
# mergeSort(ar)
# print("Sorted array is: ", end="\n")
# printList(ar)



# # s=input()
# # s=s.split()
# # mergeSort(s)

# def mergeSort(array):
#     if len(array) > 1:
#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]

#         mergeSort(L)
#         mergeSort(M)

#         i = j = k = 0

#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1


# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()

# if __name__ == '__main__':
#     array = [1, 4, 2, 98, 43, 67]

#     mergeSort(array)

#     print("Sorted array is: ")
#     printList(array)

# file = open("Vedansh.txt","r")


def user_input(n):

  # taking first number with which comparisons need to be made
  f=int(input())
  found=False
  if(len(str(f))==2):
    print("No isomorphic")
    return

  # taking the remaining numbers from the user to check if they are isomorphic with the first number
  for i in range(0,n-1):
    num=int(input())

    # checking if the number is isomorphic and printing the same if found isomorphic
    if(isIsomorphic(f,num)):
      if(found==False):
        print(f)
      print(num)
      found=True
      

  # if no number comes out to be isomorphic with respect to the first number then printing No isomorphic 
  if(found==False):
    print('No isomorphic')

def isIsomorphic(f,num):

  # changing number to strings to get easy access to digit indices
  f=str(f)
  num=str(num)
  
  dict_f = {}
  dict_num = {}
  
  f_index = 0
  num_index = 0

  # parsing the string to make a list of indices at which that particular digit occur for first number
  for i in f:
    dict_f[i] = dict_f.get(i,[]) + [f_index]
    f_index+=1

  # parsing the string to make a list of indices at which that particular digit occur for other numbers
  for j in num:
    dict_num[j] = dict_num.get(j,[]) + [num_index]
    num_index+=1

  # comparing the sorted list of values
  if(sorted(dict_f.values())==sorted(dict_num.values())):
    return True
  else:
    return False


# taking number of inputs user wants to enter
user_input(int(input()))

