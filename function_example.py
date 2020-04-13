def greetUser(firstName, lastName):
    print(f"Hi {firstName} {lastName}")
    print("Welcome to function example!!")

def squire(number):
    return number * number;

greetUser(firstName="Vinay", lastName="Kumar")
greetUser("John", "Smith")
greetUser("Peter", lastName="Smith")

print(squire(5))
