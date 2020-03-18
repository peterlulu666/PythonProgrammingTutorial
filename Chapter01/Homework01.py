def frequency(grades_list):
    count = dict()
    for grade in grades_list:
        if grade not in count:
            count[grade] = 1
        else:
            count[grade] = count[grade] + 1
    return count


def main():
    grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
    dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
    herding_dogs = dog_breeds[0:2]
    tiny_dogs = dog_breeds[-1]
    print(frequency(grades))
    print(herding_dogs)
    print(tiny_dogs)
    print("Persian" in dog_breeds)


main()
