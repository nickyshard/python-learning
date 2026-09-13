def main():
    mes = input("¿Cuánto ganas al mes? ")
    anual = calculator(mes)
    print(anual)


def calculator(m):
    m = float(m.removesuffix("€"))
    a12 = m * 12
    a14 = m * 14
    resultado = str(
        "Ganas "
        + f"{a12:,}"
        + "€ al año en 12 pagas y "
        + f"{a14:,}"
        + "€ en 14 pagas."
    )
    return resultado


main()
