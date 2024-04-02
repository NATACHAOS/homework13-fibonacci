fib1 = fib2 = 1  # с помощью for

n = int(input('Номер элемента ряда Фибоначчи: '))

print(fib1, fib2, end=' ')


for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
print()


fib1 = fib2 = 1  # c помощью while

n = input('Номер элемента ряда Фибоначчи: ')
n = int(n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print('Значение этого элемента: ', fib2)


def fibonacci(n = int(input('Номер элемента ряда Фибоначчи: '))):  # с помощью рекурсии
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print('Значение этого элемента: ', fibonacci())
