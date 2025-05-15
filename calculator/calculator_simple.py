num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))
operacion = input("Que operacion desea realizar? +, - , *, / ?: ")

if num2 == 0 and operacion == "/":
    print("Error, no se puede dividir entre 0")
else:
    if operacion == "+":
        resultado = num1+num2
        print(f"El resultado de la operacion es: {resultado}")
    elif operacion == "-" :
        resultado = num1-num2
        print(f"El resultado de la operacion es: {resultado}")
    elif operacion == "*":
        resultado = num1*num2
        print(f"El resultado de la operacion es: {resultado}")
    elif operacion == "/":
        resultado = num1/num2
        print(f"El resultado de la operacion es: {resultado}")
    else:
        print("Error. Introduce una operación válida")
