def sortNumbers(numbers):
    i = 0
    while i < len(numbers):
        j = 0
        while j < len(numbers) - i - 1:
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j + 1]
                numbers[j + 1] = numbers[j]
                numbers[j] = temp
            j += 1
        i += 1
    return numbers

def get_median(numbers):
    if numbers:
        index = int(len(numbers) / 2)
        median = numbers[index]
        if index and index * 2 == len(numbers):
            median = (median + numbers[index - 1]) / 2
    return median

numbers = []
total = 0
lowest = highest = None

while True:
    line = input("enter a number or Enter to finish: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        numbers += [number]
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    else:
        break

print("numbers: ", sortNumbers(numbers))
if numbers:
    print("count = ", len(numbers), "sum = ", total, "lowest = ", lowest,
          "highest = ", highest, "mean = ", total / len(numbers), "median = ", get_median(numbers))


