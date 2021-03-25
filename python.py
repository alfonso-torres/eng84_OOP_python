from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()

        self.large = True
        self.two_lungs = True
        self.venom = False # Polymorphism

    def clim(self):
        return "up we go ..."

    def sollow(self):
        return " can not be bothered to chew"

# python_object = Python()
# print(python_object.clim()) # clim() from Python class
# print(python_object.use_tongue_to_smell()) # use_tongue_to_smell() from Snake class
# print(python_object.hunt()) # hunt() is from reptile class
# print(python_object.breath()) # breath() is from Animal class

# Polymorphism:
# We initialize the attribute venum in the class python like we did in snake, we are overridden from the parent class
# so if we want to use this attribute, it will use the one defined in the child class
#print(python_object.venom)
