str=input()
#product of all digits in the number entered
p=1
for i in range(len(str)):
    p=p*int(str[i])
print(p)
#A supermarket maintains a pricing format for all its products, A value N is printed on each product. When the scanner reads the value N on the item, the products of all the digits in the value N is the price of the item. The task here is to design the software such that given the code for any item N the product (multiplication) of all the digits of value should be computed (price).