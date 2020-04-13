def square(number):
    return number * number


def findLargestNumberInList(numbers):
    maximum = 0;
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
