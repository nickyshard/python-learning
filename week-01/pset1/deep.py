def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    print(check(answer))


def check(a):
    match a:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"


main()