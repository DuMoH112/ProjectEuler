import time

tic = time.time()


def main():
    sumkvad = 0
    kvadsum = 0
    for i in range(1,101):
        sumkvad += i * i
        kvadsum += i
    kvadsum *= kvadsum
    print("Разность квадрата суммы и суммы квадратов: ", kvadsum - sumkvad)


def timerange(toctic):
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main();
toc = time.time()
timerange(toc - tic);
