
try:
    age = int(input("Enter Age> "))
    risk = 20000 / age
    print(risk)

    # Raise is used to throw error from block
    # raise ValueError

# except handles particular error
except ZeroDivisionError:
    print("Age should not be zero")
except ValueError:
    print("Value should be numeric only")

# finally always executes
finally:
    print("Finally....")
