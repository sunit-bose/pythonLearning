#Print a invitation with first and last names as user inputs and then concat the inputs to print result in the following format
  #>> Hello John doe!. Welcome to the python program.


a = input("Enter your first name: ")
b = input("Enter your last name: ")

c = a + " " + b

print (("Hello, %s! Welcome to the Python program.") % c)
