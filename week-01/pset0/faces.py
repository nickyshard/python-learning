def main():
    text = input()
    text = convert(text)
    print(text)


def convert(inputtext):
    outputtext = inputtext.replace(":)", "🙂").replace(":(", "🙁")
    return outputtext


main()
