def main():
    filename = input("File name: ")
    print(format(filename))


def format(file):
    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg"):
        return "image/jpg"
    elif file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "txt/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
