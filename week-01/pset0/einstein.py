def main():
    mass = input("m= ")
    energy = calculator(mass)
    print(energy)


def calculator(mass):
    mass = int(mass)
    csq = pow(300000000, 2)
    energy = mass * csq
    return energy


main()
