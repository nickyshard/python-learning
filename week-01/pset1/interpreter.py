def main():
    x, y, z = input("Expresion: ").split(" ")
    if y not in ("+", "-", "*", "/"):
        print("Invalid input")
    elif y == "/" and z == "0":
        print("Invalid input")
    else:
        print(calculator(x, y, z))


def calculator(x, y, z):
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z


main()
