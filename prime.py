x=input("enter number")
flag=0
for num in range(1,int(x)):
    x=int(x)/num
    flag=flag+1
if flag==2:
    print("number is prime")
else:
    print("not prime")