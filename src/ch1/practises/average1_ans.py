inputNumbers = []
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
        inputNumbers += [number]
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    else:
        break

print("numbers: ",inputNumbers)
if inputNumbers:
    print("count = ", len(inputNumbers), "sum = ", total, "lowest = ", lowest,
          "highest = ", highest, "mean = ", total / len(inputNumbers))