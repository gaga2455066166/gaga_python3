def CountDigit(number,digit ):
    str_numbers = str(number)
    str_number = str(digit)
    count = 0
    for i in str_numbers:
        if i == str_number:
            count+=1
    return count