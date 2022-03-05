a_file = open("words.txt")
file_contents = a_file.read()
words = file_contents.splitlines()


def find_word(word: str, list_of_words: list):
    if word.lower() in list_of_words:
        return True


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


def not_contains(letters: str, list_of_words: list):
    for word in list_of_words:
        if word.contains()


if __name__ == "__main__":
    #print(not_contains("ant", words))
    x = contains_at_index("r", 1, words)
    y = contains_at_index("n", 3, x)
    z = contains_at_index("e", 4, y)
    print(z)

    #print(contains("eav", words))
    #print(find("learn", words))


#    matches = [x for x in list_of_words if x not in matches]
