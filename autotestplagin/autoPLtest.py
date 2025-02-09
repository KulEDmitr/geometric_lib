def add(a: int, b: int) -> int:
    return a + b

def reverse_string(s: str) -> str:
    return s[::-1]

def is_even(n: int) -> bool:
    return n % 2 == 0

def find_max(lst: list[int]) -> int:
    if not lst:
        raise ValueError("Список не должен быть пустым")
    return max(lst)

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]
