import time
from math import sqrt

tic = time.time()


def main():
    flag = 0
    lst = range (1, 21)
    number = 10
    while flag == 0:
        for i in lst:
            if number % i != 0:
                number += 10
                break
            if (i == 20) and (number % 20 == 0):
                flag = 1
                break
    print(number, " самое маленькое число, которое делится без остатка на все числа от 1 до 20")

def timerange(toctic):
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);
