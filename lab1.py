def fibonacci(n):
    fib_sequence = [0, 1]  # Початкова послідовність з чисел Фібоначчі

    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]

if __name__ == "__main__":
    n = int(input("Введіть кількість чисел Фібоначчі: "))

    if n <= 0:
        print("Кількість чисел має бути більша за 0.")
    else:
        fibonacci_sequence = fibonacci(n)
        print("Послідовність Фібоначчі:", fibonacci_sequence)
