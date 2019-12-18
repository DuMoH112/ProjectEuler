import timeit
from time import time


tic = time()


def main():
    a = range(1, 1000)
    sum = 0
    for i in a:
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    print('Сумма: ', sum)


def timerange(toctic):
    toctic
    print("Время выполнения функции main: ", "	{:.6f}".format(toctic), " секунд")


main();
toc = time()
timerange(toc - tic);