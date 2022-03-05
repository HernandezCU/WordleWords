a_file = open("words.txt")
file_contents = a_file.read()
words = file_contents.splitlines()


def notin(c, list_of_words):
    x = []
    for word in list_of_words:
        if c not in word:
            x.append(x)

    return x


if __name__ == "__main__":
    global p
    while True:
        char = input("Enter Letter: \n").split()
        p = notin(char, words)
