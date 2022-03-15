import math


def prime(n: int) -> bool:
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def select_primes(tab: list[int]) -> list[int]:
    acc = []
    for number in tab:
        if prime(number):
            acc.append(number)
    return acc




