from note import Notebook
from menu import Menu
print("\n" + 100*"-")
print("The dir() function for Notebook - shows all of the attributes and methods of an object")
print("dir() function for Notebook \n", dir(Notebook))
print("\n" + 100*"-")
print("isinstance() function - returns True if the object belongs to a specific class.")
some_object = Notebook()
print("some_object = Notebook()")
print("isinstance(some_object, Notebook)" + "\n", isinstance(some_object, Notebook))
print("\n" + 100*"-")
print("\n", some_object.__class__.__dict__)
print("Attributes of a class, as we can see are just a dictionary")
print("of all of the properties of the class and the module where ")
print("an instance of class is stored.")
print("\n" + 100*"-")
print("""self represents the instance of the class. By using the “self” keyword we can access\n
        the attributes and methods of the class in python. \n
        It binds the attributes with the given arguments.""")

print("\n" + 100*"-")
print(""""__init__" is a reserved method in python classes. \n
            It is known as a constructor in object oriented concepts.\n
             This method called when an object is created from the class and \n
              it allow the class to initialize the attributes of a class""")

print("\n" + 100*"-")
print("""__str__ is the built-in function in python, \n
        used for string representation of object. \n
        __repr__ is another built-in which is similar to __str__""")
print("\n" + 100*"-")