class Animal:
    def noise(self):
        print("Animal is making noise...")


class Dog(Animal):
    pass
   # pass keyword is used if class is empity


class Cat(Animal):
    pass

class Elephant(Animal):
    def noise(self):
        print("Elephant is making noise...")


dog = Dog()
dog.noise()

cat = Cat()
cat.noise()

elephant = Elephant()
elephant.noise();