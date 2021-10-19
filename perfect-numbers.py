# This program calculates perfect numbers lower than a N given parameter.

from datetime import datetime
from math import sqrt
import multiprocessing


def execution_time(func):
    """Decorator to print in console the execution time of the 'func' function passed."""
    def wrapper(*args, **kwargs):
        t0 = datetime.now()
        res = func(*args, **kwargs)
        t1 = datetime.now()
        print(f"\nExecution time of '{func.__name__}' was: {t1-t0}")
        return res
    return wrapper


def find_divisors_v1(n):
    """Finds all divisors for a given number 'n' different than that number."""
    if n == 1:
        return [1]
    return [x for x in range(1, n) if n%x == 0]


def find_divisors_v2(n):
    """Finds all divisors for a given number 'n' different than that number."""
    # Due the fact divisors of a given N number always 'came in pairs' (that is, 
    # we can multiply then in pairs, or certain divisors by itself, to get the 
    # original number), we can search divisors M lower than sqrt(N) and then 
    # calculate it's 'pair' with N/M.
    l = int(sqrt(n)) + 1
    divisors = [1]
    for m in range(2, l):
        if n % m == 0:
            if m**2 == n:
                divisors.append(m)
            else: 
                divisors += [m, int(n/m)]
    return divisors


@execution_time
def perfect_numbers_v1(n):
    return [x for x in range(2, n+1) if sum(find_divisors_v1(x)) == x]


@execution_time
def perfect_numbers_v2(n):
    return [x for x in range(2, n+1) if sum(find_divisors_v2(x)) == x]

def is_perfect(n):
    divisors = find_divisors_v2(n)
    if sum(divisors) == n:
        print(n)


@execution_time
def perfect_numbers_v3(n):
    numbers_to_evaluate = [x for x in range(2, n+1)]
    with multiprocessing.Pool() as pool:
        pool.map(is_perfect, numbers_to_evaluate)


def run():
    n = int(input("Dime un número: "))
    # d = execution_time(find_divisors_v1)(n)
    # for i in d:
    #     print(i)
    # d = execution_time(find_divisors_v2)(n)
    # for i in d:
    #     print(i)
    # pn = perfect_numbers_v1(n)
    # for i in pn:
    #     print(i)
    # pn = perfect_numbers_v2(n)
    # for i in pn:
    #     print(i)
    perfect_numbers_v3(n)


if __name__ == '__main__':
    run()