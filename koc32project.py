import random
a=int(input("A="))
b=int(input("B="))
r=random.randint(a,b)
# list1=[]
# for i in range(a,b+1):
#     list1.append(i)
# r=random.choice(list1) 

if r%2==0:
    print(r,"is a even no")
if r%2!=0:
    print(r,"is a odd no")
if r>=0:
    print(r,"is a positive no")    
if r<0:
    print(r,"is a negative no")
if r>1:
    for i in range(2,r):
        if r%i==0:
            print(r,"is a composite no")
            break
    else:
        print(r,"is a prime no") 
else:
    print(r,"is a composite no")          