a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите действие ")

def result(a, b, c):
    if c == "+":
        res = a + b
        print(res)
    elif c == "-":
        res = a - b
        print(res)
    elif c =="*":
        res = a*b
        print (res)
    else:
        print("Неизвестное действие")

result(a, b, c)