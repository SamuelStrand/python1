def calc(number1, number2, oper):
    print(number1, number2, oper)
    if oper == "+":
        return number1 + number2
    if oper == "-":
        return number1 - number2
    if oper == "*":
        return number1 * number2
    if oper == "/":
        if number2 != 0:
            return number1 / number2
        else:
            print("Вы ввели ноль")
    if oper == "**":
        return number1 ** number2
    if oper == "//":
        if number2 != 0:
            return number1 // number2
        else:
            print("Вы ввели ноль")
            return (print("Введите другое число"))
    import math
    if oper == "math.sqrt":
        return math.sqrt(number1), math.sqrt(number2)
    if oper == "%":
        return number1 % number2




result = calc(10, 3, "+")
print(result)

result = calc(10, 3, "-")
print(result)

result = calc(10, 3, "*")
print(result)

result = calc(10, 0, "/")
print(result)

result = calc(10, 3, "**")
print(result)

result = calc(10, 3, "//")
print(result)

result = calc(64, 144, "math.sqrt")
print(result)

result = calc(10, 4, "%")
print(result)






