a = float(input())
op = input()
b = float(input())

try:
    res = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
    print(f"{res[op]:.2f}")
except:
    print("divided by zero")