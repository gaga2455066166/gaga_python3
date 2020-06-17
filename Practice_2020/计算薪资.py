def bonus(sales):
    x = 5000
    if sales <= 10000:
        return x
    elif 10000 < sales <= 20000:
        return x + sales * 0.1
    elif 20000 < sales <= 50000:
        return x + sales * 0.15
    elif 50000 < sales <= 100000:
        return x + sales * 0.2
    elif 100000 < sales:
        return x + sales * 0.25
