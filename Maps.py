

def sq(a):
     return a*a

def cb(a):
     return a*a*a

funcs = [sq,cb]
num = [2 , 4 , 10 , 19 , 28 , 44 , 65]
for i in range (len(num)):
    val = list(map(lambda x : x(i),funcs))

    print (val)
