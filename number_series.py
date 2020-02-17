a=int(input('Enter the value'))
b=int(input('Enter the value'))
if(a>b):
    for i in range(a,b,-1):
        print(i)
else:
    for i in range(a,b,1):
        print(i)
    
