'''
refer : https://www.geeksforgeeks.org/python-operators/
for theory
'''

#problem 1: Input two integers and do the following arithmetic operations : +, -, *, /, %, **
#sol:

a = int(input('enter a: '))
b = int(input('enter b: '))
print(a,"+",b,"=",(a+b)) #normal method
print('{x} + {y} = {z}'.format(x=a,y=b,z=(a+b))) #string formating
print(f'{a} + {b} = {(a+b)}') #string formating method 2
print(f'{a} - {b} = {(a-b)}') #sub
print(f'{a} * {b} = {(a*b)}') #mul
print(f'{a} / {b} = {(a/b)}') #div
print(f'{a} % {b} = {(a%b)}') #rem
print(f'{a} ** {b} = {(a**b)}') #power


