import pandas
dataFrame = pandas.read_csv('insurance.csv')
curr_date = input()
make = input()

print(dataFrame)

l_male = []
l_female = []
gen_index = 0
for i in list(dataFrame['Gender']):
    if(i=='Male'):
        l_male.append(gen_index)
    else:
        l_female.append(gen_index)
    gen_index+=1
print()
# Part 1
for i in l_male:
    print(list(dataFrame['Insurance No'])[i],end=" ")
print()
# Part 2
for i in l_female:
    print(list(dataFrame['Name of the Owner'])[i],end=" ")
print()
# Part 3
from datetime import datetime

date_index = 0
for i in list(dataFrame['Last Policy Issued On Date']):
    last_date = i

    start = datetime.strptime(last_date, "%d/%m/%Y")
    end =   datetime.strptime(curr_date, "%d/%m/%Y")
    
    
    diff = end.date() - start.date()
    
    if(diff.days>=365):
        print(list(dataFrame['Name of the Owner'])[date_index], list(dataFrame['Vehicle Identification No.'])[date_index])
    
    date_index+=1
    
# Part 4
make_index = 0;
for i in list(dataFrame['Make of the Vehicle']):
    if(i == make):
        print(list(dataFrame['Name of the Owner'])[make_index],end=" ")
    make_index+=1