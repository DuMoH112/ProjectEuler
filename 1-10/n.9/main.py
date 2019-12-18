import time
from math import sqrt

tic = time.time()


def main():
    a = [0, 0, 0]

    for a[0] in range(1, 500):
        for a[1] in range(1, 500):
            a[2] = int(sqrt(a[0] ** 2 + a[1] ** 2))
            if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
                if a[0] + a[1] + a[2] == 1000:
                    print(a[0], ' + ', a[1], ' == ', a[2])
                    print(a[0] ** 2, ' + ', a[1] ** 2, ' == ', a[2] ** 2)
                    print(a[0] * a[1] * a[2])
                    print()


def timerange(toctic):
    print()
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main()
toc = time.time()
timerange(toc - tic)
