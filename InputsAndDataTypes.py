desiredInput = input("message for the user")
print(desiredInput)

#taking input in next line:
desiredInput = input("message for the user \n")
print(desiredInput)

'''
DataTypes in Python

Text : str
Numeric : int, float, complex
Sequence : list, tuple, range
Mapping type : Dictionary - dict
Set types : set
Boolean type : bool

Basic datatypes - str, int, float, complex & bool
Advanced datatypes - dict, set, range, list, tuple

the datatype can be found by using - type()

'''

a = 2
a = a + a #variable - so it can be changed and a will be 4 now
print(a) # expected output - 4
print(type(a)) # will output the type of a as 'int'
b = 2.2
print(b)
print((type(b))) #output - float
print(a+b) #6.2
print((type(a+b))) #resultant would be float


#input always returns string
x = input("enter a number \n")
y = input("enter a number \n")
print(x+y) #suprise :)

#type casting methods: int(), float(), complex()
p = int(input())
q = int(input())
print(p+q) #will print integer

