"""
Morgyn Stryker
2/15/2016
"""
import math


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    if is_even(number):
        return False

    sqrt_n = int(math.sqrt(number) + 1)
    for i in range(3, sqrt_n, 2):
        if number % i == 0:
            return False

    return True


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def print_successive_primes(number_of_primes, start_number=1):
    prime_generator = get_primes(start_number)
    for i in range(number_of_primes):
        print '{}: {}'.format(i+1, prime_generator.next())


def main():
    print_successive_primes(50)


if __name__ == '__main__':
    main()
