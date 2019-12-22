import time

tic = time.time()

class MyClass:

    def __init__(self, x, y):
       self.width = x
       self.height = y

    def factorial(self, n):
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact 

    def vivod(self):
        print (int(self.factorial(self.width)/(self.factorial(self.height)*self.factorial(self.width-self.height))))   
    

def main():
    obj = MyClass(20+20, 20)
    obj.vivod()
    


def timerange(toctic):
    print()
    print("Время выполнения функции main: ", "{:.6f}".format(toctic), " секунд")


main()
toc = time.time()
timerange(toc - tic)