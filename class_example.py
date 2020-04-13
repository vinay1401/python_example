class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing at ({self.x}, {self.y})")

    def sketch(self):
        print(f"Sketching at ({self.x}, {self.y})")


point = Point(10, 20)
print(point.x)
point.draw()
point.sketch()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi I am {self.name}')


john = Person("John Smith")
john.talk()