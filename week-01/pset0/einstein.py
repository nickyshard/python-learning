def main():
    num = input("m= ")
    num = calculator(num)
    print(num)


def calculator(mass):
    mass = int(mass)
    csq = pow(300000000, 2)
    energy = mass*csq
    return energy

main()