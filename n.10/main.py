import time

tic = time.time()

def summa(list):
    sum = 0
    for i in list:
        sum += i
    return (sum - list[len(list)-1])

def main():
    lst = [2]
    i = 3
    a = len(lst)
    while lst[a-1] < 2000001:
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
    print(a, " простое число: ", lst[a - 1])
    print(summa(lst))


def timerange(toctic):
    print()
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main()
toc = time.time()
timerange(toc - tic)
