#Creating a function
#def my_function():
#    print("Hello, I'm a function")

# Calling a function
#my_function()

#Arguments
#def my_function(fname, lname):
#    print(fname + " " + lname)

#my_function("Emil", "Refsnes")

#Arbitary Arguments
#def this_is_a_function(*kids):
#    print("The youngest child is " + kids[2])

#this_is_a_function("Emil", "Tobias", "Anthony", "Elliott")

#Keyword Arguments
#def major_function_example(child3, child2, child1):
#    print("The youngest child is " +child3)

# major_function_example(child1 = "Emil", child2= "Anthony", child3 = "Tobias")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the
#parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
    print("His last name is: " + kid["lname"])
    print("and his first name is: " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")
