def sums(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a * b
    return c


if __name__ == '__main__':
    
    a = int(input('enter no. one: '))
    b = int(input('enter no. one: '))

    sumans = sums(a, b)
    subans = sub(a, b)
    mulans = mul(a, b)
    divans = div(a, b)
    
    print('Sum:', sumans)
    print('Sub:', subans)
    print('Mul:', mulans)
    print('Div:', divans)