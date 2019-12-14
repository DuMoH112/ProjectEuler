import time
from math import sqrt

tic = time.time()


def main():
    lst = [2]
    i = 3
    while len(lst) < 10001:
        if i > 10:
            if (i % 2 == 0) or (i % 10 == 5):
                i += 2
                continue
        for j in lst:
            if (j * j - 1 > i):
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 2
        a = len(lst)
    print(a," простое число: ", lst[a - 1])


def timerange(toctic):
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);
