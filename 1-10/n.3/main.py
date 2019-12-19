import time
from math import sqrt

tic = time.time()

lst = [1]

def proverka (number, i):
    if number % i == 0:
        lst.append(i)
        return (number / i)
    else:
        return number



def main():
    number = 600851475143
    lst_all = [2]
    for i in range(3, number + 1, 2):
        if i > 10:
            if (i % 2 == 0) or (i % 10 == 5):
                continue
        for j in lst_all:
            if (j * j - 1 > i):
                lst_all.append(i)
                number = proverka(number, i)
                break
            if i % j == 0:
                break
        else:
            lst_all.append(i)
            number = proverka(number, i)
        if number == 1:
            break
    print('Самый большой делитель числа 600851475143, являющися простым числом: ', max(lst))
    print(lst)



def timerange(toctic):
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);
