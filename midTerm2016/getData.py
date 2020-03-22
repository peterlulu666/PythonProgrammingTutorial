def getData(m):
    """getData

    :param m: a astring
    :return: a string consisting of the month and day, separated by a space
    """
    month = input("What month is it? ")
    day = input("What day is it? ")
    print(month + " " + day + " " + m)
    return month + " " + day


def main():
    print(getData("is a great day!"))


main()
