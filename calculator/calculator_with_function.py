def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Error: cannot divide by zero"
        return num1 / num2
    else:
        return "Error: invalid operation"

# Entrada de usuario
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operacion = input("Choose an operation (+, -, *, /): ")

    resultado = calcular(num1, num2, operacion)
    print(f"Result: {resultado}")

except ValueError:
    print("Please enter valid numeric values.")
