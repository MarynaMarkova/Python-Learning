class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!!!")


class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")


class Lion(Cat):
    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars!!!")


c = Cat("Blue")

eli = Lion("Eli")
print(c.name)
print(c.meow())
print(eli.name)
eli.meow()
eli.roar()
