def twoWords(length, firstLetter):
    """twoWords

    :param length: the length of the first word
    :param firtLetter: the first letter of the second word
    :return: word list
    """
    twoWordList = []
    while True:
        word = input("A " + str(length) + "-letter word please ")
        if len(word) == length:
            twoWordList.append(word)
            break

    while True:
        word = input("A word beginning with " + firstLetter + " please ")
        if word.upper()[0] == firstLetter.upper():
            twoWordList.append(word)
            break
    return twoWordList


# print(twoWords(4, "B"))


def twoWordsV2(length, firstLetter):
    twoWordList = []
    while len(twoWordList) < 1:
        word = input("A " + str(length) + "-letter word please ")
        if len(word) == length:
            twoWordList.append(word)

    while len(twoWordList) < 2:
        word = input("A word beginning with " + firstLetter + " please ")
        if word.upper()[0] == firstLetter.upper():
            twoWordList.append(word)
    return twoWordList


# print(twoWordsV2(4, "B"))


def enterNewPassword():
    password = input("Enter a password")
    count = 1
    while True:
        # Including at least one digit
        if (8 <= len(password) <= 15) and any(character.isdigit() for character in password):
            print("Valid password")
            print("tried " + str(count) + " times")
            break
        else:
            print("Fail")
            count = count + 1
        password = input("Enter a password")


enterNewPassword()
