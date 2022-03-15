import tkinter
a_file = open("words.txt")
file_contents = a_file.read()
global words
words = file_contents.splitlines()



def contains(letters: str):
    matches = []
    count = 0
    for word in words:
        for letter in letters:
            if letter in word:
                count += 1
        if count == len(letters):
            matches.append(word)
        count = 0

    return matches


def contains_at_index(letter: str, index: int):
    matches = []
    for word in words:
        if word[index] == letter:
            matches.append(word)

    return matches


def not_contains(letter: str):
    x = []
    for word in words:
        if letter not in word:
            x.append(word)
        else:
            pass

    return x


def not_contains_at_index(letter: str, index: int):
    x = []
    for word in words:
        if word[index] != letter:
            x.append(word)
        else:
            pass

    return x


def remove_word(word):
    words.remove(word)
    return words


if __name__ == "__main__":
    pass

