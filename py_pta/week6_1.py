def CountDigit(numbers, digit):
    s = 0
    if numbers < 0:
        numbers = -numbers
    while numbers > 0:
        if numbers % 10 == digit:
            s += 1
        numbers = numbers // 10
    return s


number, digit = input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number, digit)
print("Number of digit 2 in " + str(number) + ":", count)
