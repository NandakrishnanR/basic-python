num1=float(input('enter 1st side'))
num2=float(input('enter 2nd side'))
num3=float(input('enter 3rd side'))
s=(num1+num2+num3)/2
area=(s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
print('area of the triangles with sides {0},{1},{2} is {3}'.format(num1,num2,num3,area))
