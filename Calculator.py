class Calc:
    
    @staticmethod
    def sum(a, b):
        c = a + b
        return c
    
    @staticmethod
    def sub(a, b):
        c = a - b
        return c


class Main:
    
    a = int(input('enter no. one: '))
    b = int(input('enter no. one: '))

    calcObj = Calc()
    calcObj.sum(a, b)
    calsObj.sub(a, b)