# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    
    def description(self):
        print(f"Name : {self.name}")
        print(f"Age :  {self.age}")
    
    def get_info(self):
        print(f"Coat_color : {self.coat_color}")

class JackRussellTerrier(Dog):

    def __init__(self,name,age,coat_color,intelligence_level):
        super().__init__(name,age,coat_color)
        self.intelligence_level = intelligence_level

    def play_fetch(self):
        print(f"{self.name} loves to play fetch!")

    def dig(self):
        print(f"{self.name} is an excellent digger!")

    def high_jump(self):
        print(f"{self.name} can jump really high!")
        

class Bulldog(Dog):

    def __init__(self,name,age,coat_color,weight):
        super().__init__(name,age,coat_color)
        self.weight=weight

    def get_weight(self):
        print(f"The weight of {self.name} is {self.weight} kg.")

    def wrinkles(self):
        print(f"{self.name}'s face has adorable wrinkles!")

    def friendly(self):
        print(f"{self.name} is a very friendly and loyal companion!")


print("*"*30)
d=Dog("Red_hood",20,"Red")
d.description()
d.get_info()

print("*"*30)
terrier = JackRussellTerrier("Rocky", 2, "White", "High")
terrier.description()
terrier.get_info()
terrier.play_fetch()
terrier.dig()
terrier.high_jump()

print("*"*30)
bulldog = Bulldog("Spike", 4, "Brown", 25)
bulldog.description()
bulldog.get_info()
bulldog.get_weight()
bulldog.friendly()
bulldog.wrinkles()
