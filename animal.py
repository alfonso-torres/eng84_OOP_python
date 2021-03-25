# Let's create are first class
# Syntax class is the key word then name of the class

# Creating an Animal class
class Animal():

    # name = "Dog" # class variable
    def __init__(self): # self refers the current class
        self.alive = True
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving left right and centre "

    def eat(self):
        return " keep eating to stay alive "

    def breath(self):
        return " keep breathing if you want to live"

# Creating an object of our Animal class

# cat = Animal() # this will store all the data available in Animal class into cat

# print(cat.eat()) # ABSTRACTION -> THE USER DOESN'T NEED TO KNOW WHAT IS HAPPENING BEHIND BUT HE JUST KNOW THAT WITH CAT HE HAS DIFFERENTS OPTIONS WITH cat.
# eat() is Abstraction

    # pass # pass is a key word used to by pass the code
