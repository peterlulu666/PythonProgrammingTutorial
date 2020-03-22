def bigCount(numberList, threshold):
    """bigCount

    :param numberList: a list of number
    :param threshold: an integer number
    :return: count integer greater than threshold
    """
    count = 0
    # Compare the first number with the threshold, if the first number is greater than threshold, increment count
    # Compare the second number with the threshold, if the second number is greater than threshold, increment count
    # Compare the third number with the threshold, if the third number is greater than threshold, increment count
    for number in numberList:
        if number > threshold:
            count = count + 1
    return count


def main():
    print(bigCount([-5, 6, 3, 0, 7], 2))


main()
