numbers = []
while True:
    number = input("Enter a number (-1 to stop): ")
    if number == '-1':
        break
    numbers.append(float(number))

sum_numbers = sum(numbers)
formatted_sum = "{:.2f}".format(sum_numbers)
print(formatted_sum)
