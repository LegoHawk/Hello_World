#default parameter value
#def my_function(country = "Norway"):
#    print("I am from " + country)
#my_function("Sweden")
#my_function("Pakistan")
#my_function()
#my_function("Brazil")
#-------
# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "mango", "banana", "cherry"]
my_function(fruits)
#------------
#return values
def my_functions(y):
    return 10 * y
print(my_functions(3))
print(my_functions(10))
print(my_functions(250))
#------------
#The pass statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

def myfunctional():
    pass