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
    :return: a list of the integers in the range from 0 to maxInt that are divisible ny both integer in twoInts
    """
    maxInt = int()
    twoInts = tuple()

