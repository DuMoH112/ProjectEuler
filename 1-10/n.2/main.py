import time


tic = time.time()


def main():
    sum = 0
    a = 1
    b = 2
    c = 0
    while a < 4000000:
        if (a % 2 == 0):
            sum += a
        c = a + b
        a = b
        b = c
    print ('Сумма чётных элементов ряда фибоначи: ', sum)

def timerange(toctic):
    toctic
    print("Время выполнения функции main: ", "	{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);