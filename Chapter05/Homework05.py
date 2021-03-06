def hasFinalLetter(strList, letters):
    """hasFinalLetter

    :param strList: a list of string
    :param letters: upper case and lower case letters
    :return: list of string that end with letter in letters
    """
    letters = letters.lower()
    wordList = []
    for word in strList:
        if word[len(word) - 1] in letters:
            wordList.append(word)
    return wordList


strList = ["computer", "science", "student"]
letters = "Et"
print(hasFinalLetter(strList, letters))


def isDivisible(maxInt, twoInts):
    """isDivisible

    :param maxInt: an integer
    :param twoInts: a tuple of two integers
    :return: a list of the integers in the range from 0 to maxInt that are divisible by both integer in twoInts
    """
    numberList = []
    for number in range(maxInt):
        if number % twoInts[0] == 0 and number % twoInts[1] == 0:
            numberList.append(number)
    return numberList


maxInt = 100
twoInts = (2, 5)
print(isDivisible(maxInt, twoInts))
