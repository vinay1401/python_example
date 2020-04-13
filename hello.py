numbers = [9,2,4,5,6,6,2,4]
numbers2 = numbers.copy()
uniqueNumbers = []

numbers.sort();

for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number);

print(numbers)

for number in numbers2:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)

print(uniqueNumbers)