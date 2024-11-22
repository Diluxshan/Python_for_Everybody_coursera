numberss = [2,4,34,7,20,5,8,29,1, 70]


def identify_max(numbers):
    maxnum = 0

    for number in numbers:
        if maxnum < number:
            maxnum = number
        else:
            maxnum = maxnum

    return maxnum

print(identify_max(numberss))