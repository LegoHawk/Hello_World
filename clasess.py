# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5


# Now we can use the class named MyClass to create objects:

p1 = MyClass()
print(p1.x)

# Objects can also contain methods. Methods in objects are functions that belong to the object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        #print("Hello! My name is", self.name, "and I am", self.age, "years old.") #traditional way of writing line
        print(f"Hello! My name is {self.name}, and I am, {self.age} years old") #using f-strings, so much easier

p1 = Person("John", 36)
p2 = Person("Sally", 30)
p1.myfunc()
p2.myfunc()
