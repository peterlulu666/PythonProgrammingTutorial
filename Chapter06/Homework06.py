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


print(twoWords(4, "B"))
