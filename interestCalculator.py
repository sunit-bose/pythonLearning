'''
f = input("enter a value: ")
f = float(f)
c = (f-32)*5/9
print (c)
'''

#Simple interest calculator

p = input("Enter principle amount: ")
p = float(p)
r = input("Enter Rate of interest: ")
r = float(r)
t = input("Enter tenure: ")
t = float (t)

SI = (p*r*t)/100

print ("The simple interest on the principle is: ", SI)
