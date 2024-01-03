class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} lives in {self.habitat}"

    def make_baby(self):
        pass

    def move(self):
        pass


class Mammal(Animal):
    def __init__(self, name, habitat, number_legs=0):
        super().__init__(name, habitat)
        self.number_legs = number_legs

    def make_baby(self):
        print("Gives birth to little animal")

    def move(self):
        print("Usually runs")


class Bird(Animal):
    def __init__(self, name, habitat, wingspan=0):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def make_baby(self):
        print("Makes eggs")

    def move(self):
        print("Usually flies")


class Fish(Animal):
    def __init__(self, name, habitat, length=0):
        super().__init__(name, habitat)
        self.length = length

    def make_baby(self):
        print("Makes eggs but in water")

    def move(self):
        print("Usually swims")


if __name__ == "__main__":
    mammal = Mammal('cal', 'Romania', 4)
    print(mammal)
    mammal.make_baby()
    mammal.move()


