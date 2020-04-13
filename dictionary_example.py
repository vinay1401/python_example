user = {
    "name": "Vinay Kumar",
    "age": 30,
    "country": "India"
}

print(user.get("dob"), "14 Jan 1988")

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

numInput = input("Enter Numbers: ")

for num in numInput:
    print(numbers.get(num))