import time
from math import sqrt

tic = time.time()


def reverse(number_2):
    if number_2 < 10:
        return (number_2 * 100)
    elif number_2 == 10:
        return 10
    elif number_2 < 100:
        return ((int(number_2 % 10) * 100) + int(number_2 / 10) * 10)
    elif number_2 == 100:
        return 1
    elif number_2 > 100:
        n1 = int(number_2 % 10)
        number_2 = int(number_2 / 10)
        return ((n1 * 100) + ((number_2 % 10) * 10) + int(number_2 / 10))


def main():
    palindrom = []
    number_1 = 0
    number_2 = 0
    temp = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            temp = i * j
            number_1 = int(temp / 1000)
            number_2 = int(temp % 1000)
            number_2 = reverse(number_2)
            if number_1 == number_2:
                number_1 = i
                number_2 = j
                palindrom.append(i * j)
                break
    print("Самый большой палиндром 3х значного числа: ", max(palindrom))
    print("Он состоит из множителей ", number_1, " и ", number_2)


def timerange(toctic):
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);
