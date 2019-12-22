import time

tic = time.time()


class MyClass:

    def __init__(self):
        self.number = [2, 1]
        self.numberMax = 0
        self.index = 0
        self.indexMax = 0
        self.arrayNumber = []
        self.arrayNumberMax = []
    
    def fun(self):
        for i in range(1000000 - 3):
            self.number[0] += 1
            self.number[1] = self.number[0]
            self.index = 0
            self.arrayNumber = [self.number[1]]

            while self.number[1] > 1:
                if self.number[1] % 2 == 0:
                    self.number[1] /= 2
                    self.index += 1
                else:
                    self.number[1] = 3 * self.number[1] + 1
                    self.index += 1
                self.arrayNumber.append(int(self.number[1]))
            if self.index > self.indexMax:
                self.indexMax = self.index
                self.numberMax = int(self.number[1])
                self.arrayNumberMax = self.arrayNumber
        print(self.number)
        print(self.index + 1)
        print(self.numberMax)
        print(self.arrayNumberMax)          
        

def main():
    obj = MyClass()
    obj.fun()


def timerange(toctic):
    print()
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main()
toc = time.time()
timerange(toc - tic)