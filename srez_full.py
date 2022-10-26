# Maxim Denisov, Srez #1

# 1 TASK

x = int(input("Введите координаты x: "))
y = int(input("Введите коордианты y: "))
if (x > 0) and (y > 0):
    print("Первая четверть")
elif (x < 0) and (y > 0):
    print("Вторая четверть")
elif (x < 0) and (y < 0):
    print("Третья четверть")
else:
    print("Четвертая четверть")

# 2 TASK

word = float(input("Введите число: "))
sum = 0
while word > 0:
    digit = word % 10
    sum = sum + digit
    word = word // 10
print(sum)

# 3 TASK

list = [1, 3, 4, 8, 6, 23, 4, 3, 5, 64, 9]
sum = 0
for i in range(0, len(list)):
    if i % 2 == 0:
        sum += list[i]
print(sum)

# 4 TASK 

def math_operation(a, b, char):
    result = 0
    if char == "+":
        result = a + b
    elif char == "-":
        result = a - b
    elif char == "*":
        result = a * b
    elif char == "/":
        result = a / b
    else:
        return "Неизвестная операция"
    return result
print(math_operation(3, 3, "-"))
        

