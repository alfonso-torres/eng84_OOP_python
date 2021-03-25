# Let's import reptile class

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.fork_tongue = True

    def use_tongue_to_smell(self):
        return  " I use my tongue to smell "

    def shed_skin(self):
        return  " growing out "

# snake_object = Snake()

# print(snake_object.eat()) # eat() is inherited from the Animal class
# print(snake_object.move()) # move() is inherited from the Animal class
# print(snake_object.hunt()) # hunt() is inherited from Reptile class
# print(snake_object.use_tongue_to_smell()) # use_tongue_to_smell() is from current class
# Multiple inheritance
# Encapsulation: you can create any attribute or function private -> __name_attribute or __function_attribute
# It will belong only in the class that you defined and anyone can not access to them.
