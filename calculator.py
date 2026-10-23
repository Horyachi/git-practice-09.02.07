def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Division by zero is not allowed')
    return a / b

if __name__ == '__main__':
    print(add(2, 3))
    print(multiply(2, 3))
    print(divide(10, 2))
