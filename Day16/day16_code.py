# Challenge - Generate the first n Fibonacci numbers with a generator

def fibonacci_generator(n):
    a, b = 0, 1
    for f in range(n):
        yield a
        a,b = b, a+b


n = int(input("Enter how many Fibonacci numbers you want: "))
for fib in fibonacci_generator(n):
    print(fib, end = " ")
