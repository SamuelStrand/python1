def calc(number1, number2, oper):
    print(number1, number2, oper)
    if oper == "+":
        return number1 + number2
    if oper == "-":
        return number1 - number2


result = calc(10, 3, "+")
print(result)
result = calc(-11, -5, "+")
print(result)
result = calc(10, 3, "-")
print(result)

