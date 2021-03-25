# Python OOP

Object-Oriented programming (OOP) is a method of structuring a program by building 
related properties and behaviors into individual objects. It is a programming paradigm that
provides a means of structuring programs so that properties and behaviors are bundled into 
individual objects. <br/>
For instance, an object could represent a person with <u>properties</u> like
a name, age, and address and <u>behaviors</u> such as walking, talking and running.

## Why OOP
It is exceptionally valuable for the reason that it permits you to bundle together
information states and functionality to alter those information states, whereas 
keeping the subtle elements hidden away. As a result, code with OOP plan is adaptable,
measured, and abstract. So this makes it especially valuable after you make bigger programs.

### Four pillars of OPP with use cases
You can apply OOP in your code with classes and objects. All the objects
you create will have states and functionality.<br/>
There are four major benefits to OOP. There are four pillars:
- *Abstraction*:

By using classes, you will be able to generalize your objects types, simplifying 
  your program. So as a developer we will show only the essential features of the
  application and hiding the details from the user. Let's see an example:
````python
class Animal():

    def __init__(self): # self refers the current class
        self.alive = True
        self.spine = True

    def eat(self):
        return " keep eating to stay alive "
        
# Creating an object of our Animal class
cat = Animal() # this will store all the data available in Animal class into cat
print(cat.eat())  # eat() is Abstraction
# THE USER DOESN'T NEED TO KNOW WHAT IS HAPPENING BEHIND
````
- *Encapsulation*:

In OOP, you bundle code into a single unit where you can determine the scope of 
each piece of data. It means that is all about binding the data variables and 
functions together in class. It helps us to make data private from the customer.
Let's see an example:
````python
# Creating a Snake class
class Snake(Reptile):

    def __init__(self):
        # Protected member
        self.__fork_tongue = True

# Creating an object of our Snake class
snake_object = Snake()
print(snake_object.__fork_tongue)
# It will result in Attribute Error because we made the attribute __fork_tongue private
# So we can see that it is encapsulated to the user
````  
- *Inheritance*:

A class can inherit attributes and behaviors from another class, so we will be able
to reuse more code. The class which is inherited from, is called the base class, and the class 
which inherits the code from the base class is called a Parent class. Let's see an example:
````python
# Creating an Animal class
class Animal():

    def __init__(self): # self refers the current class
        self.alive = True

    def breath(self):
        return " keep breathing if you want to live"

# Let's import Animal class

from animal import Animal # this is to ensure Animal class is inherited
class Reptile(Animal): # We need to pass the animal class as an arg in our Reptile class

    def __init__(self):
        super().__init__() # super is to make everything available from parent class
        self.cold_blooded = True

    def hunt(self):
        return " working hard to catch the next meal "

# Let's see amazing benefits of inheritance
reptile_object = Reptile()
# We can use the method "breath()" from the class Animal() because is inherited
print(reptile_object.breath())

````
- *Polymorphism*:

One class can be used to create many objects, all from the same flexible piece of code.
So you can inherit from parent class as well as override the data. It allows us to create
attributes and methods with the same name which will perform differently. Let's see an example:
````python
# Creating an Snake class
class Snake(Reptile):

    def __init__(self):
        self.venom = True

# Let's import Snake class
from snake import Snake # this is to ensure Snake class is inherited
class Python(Snake): # We need to pass the Snake class as an arg in our Python class

    def __init__(self):
        super().__init__()

        self.venom = False # Polymorphism

# Creating an object of our Python class
python_object = Python()
print(python_object.venom)
# It will print "False". We inherit the attribute "venom" from our Parent class.
# But in the Python class we are overriden this attribute.
# So the program will use the attribute from this class, not from Parent class.
````
## <u>NOTE</u>:
To analyze better all the concepts that we have covered in this file, we can 
analyze the image "OOP_python", as well as the code files "animal.py", 
"reptile.py", "snake.py" and "python.py" related to the image. In this way 
we can understand what OPP is and what its four pillars are.
