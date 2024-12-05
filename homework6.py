class Animal:
    def __init__(self, name, age, species, sound):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound
        self.get_attrs()

    def get_attrs(self):
        print(self.__dict__)

    def __str__(self):
        return f"{self.name} ({self.species}), {self.age} років"

    def make_sound(self):
        print(f"{self.sound}")


dog = Animal(name="Bobik", age=10, species="Dog", sound="bark")
dog.make_sound()
cat = Animal(name="cat", age=5, species="Cat", sound="miau")
cat.make_sound()


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.get_attr()

    def get_attr(self):
        print(self.__dict__)

    def calculate_area(self):
        solution = self.height * self.width
        print(f"Solution is: {solution}")


rec1 = Rectangle(height=12, width=10)
rec1.calculate_area()