def main():
    greeting = input("Greeting: ")
    print(payment(greeting))


def payment(g):
    if g == "hello":
        return "$0"
    elif 1 == g.startswith("h"):
        return "$20"
    else:
        return "$100"


main()
