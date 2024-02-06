number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("ingrese un numero mayor al numero previamente ingresado :"))

keeper = {}
for i in range(number1, number2 + 1):
    counter = 1
    x = i
    while x != 1:
        if x % 2 == 0:
            x = x//2
            counter += 1

        elif x % 2 != 0:
            x = (x*3) + 1
            counter += 1

        if x == 1:
            keeper[i] = counter
            break

greater_value = max(keeper.values())

for key, value in keeper.items():
    if value == greater_value:
        larger_key = key

print(f"El valor con secuencia mas larga fue {larger_key} con {greater_value}")