# Let's import Animal class

from animal import Animal # this is to ensure Animal class is inherited
class Reptile(Animal): # We need to pass the animal class as an arg in our Reptile class

    def __init__(self):
        super().__init__() # super is to make everything available from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.hart_chambers = [3,4]

    def hunt(self):
        return " working hard to catch the next meal "

    def use_venom(self):
        return "I use it if I've got "

    def seek_heat(self):
        return "looking for sunshine "

# Let's see amazing benefits of inheritance
# reptile_object = Reptile()
# Time to see the Magic of OOP
# print(reptile_object.hunt())
# print(reptile_object.breath())
