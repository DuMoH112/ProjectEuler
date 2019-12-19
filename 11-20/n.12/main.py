import time

from math import sqrt

tic = time.time()


def dividers(number):
    lst = [1]

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            lst.append(i)
            lst.append(number // i)

    return lst


def main():
    triangle_number = [1]
    list_dividers = []

    i = 2
    while len(list_dividers) < 500:
        triangle_number.append(triangle_number[i - 2] + i)

        list_dividers = dividers(triangle_number[-1])
        # print(len(list_dividers), '     ', triangle_number[-1], ': ', list_dividers)
        i += 1

    print(triangle_number[-1])
    print(list_dividers)


def timerange(toctic):
    print()
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main()
toc = time.time()
timerange(toc - tic)
