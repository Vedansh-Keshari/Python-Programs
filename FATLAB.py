def user_input(n):

  # taking first number with which comparisons need to be made
  f=int(input())
  found=False
    
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

