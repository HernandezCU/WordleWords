import tkinter
a_file = open("words.txt")
file_contents = a_file.read()
words = file_contents.splitlines()
global updated_words


def contains(letters: str, list_of_words: list):
    matches = []
    count = 0
    for word in list_of_words:
        for letter in letters:
            if letter in word:
                count += 1
        if count == len(letters):
            matches.append(word)
        count = 0

    return matches


def contains_at_index(letter: str, index: int, list_of_words: list):
    matches = []
    for word in list_of_words:
        if word[index] == letter:
            matches.append(word)

    return matches


def not_contains(letter: str, list_of_words: list):
    x = []
    for word in list_of_words:
        if letter not in word:
            x.append(word)
        else:
            pass

    return x


def not_contains_at_index(letter: str, index: int, list_of_words: list):
    x = []
    for word in list_of_words:
        if word[index] != letter:
            x.append(word)
        else:
            pass

    return x


def remove_word(word, list_of_words):
    list_of_words.remove(word)
    return list_of_words


if __name__ == "__main__":
    pass

