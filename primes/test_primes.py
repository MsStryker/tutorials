"""
Morgyn Stryker
2/15/2016
"""
from unittest import TestCase, main

import sys
from StringIO import StringIO

from primes import get_primes, is_even, is_prime, print_successive_primes


class ScratchTestCase(TestCase):

    def setUp(self):
        self.x = 1
        self.y = 2

    def test_thing_1(self):
        self.assertNotEqual(self.x, self.y)

    def test_thing_2(self):
        self.assertEqual(self.x + self.x, self.y)


class IsEvenTestCase(TestCase):

    def test_even(self):
        self.assertTrue(is_even(2))

    def test_odd(self):
        self.assertFalse(is_even(5))


class IsPrimeTestCase(TestCase):

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_three(self):
        self.assertTrue(is_prime(3))

    def test_thirty_one(self):
        self.assertTrue(is_prime(31))

    def test_one_hundred_three(self):
        self.assertTrue(is_prime(103))

    def test_one_hundred_five(self):
        self.assertFalse(is_prime(105))


class GetPrimesTestCase(TestCase):

    def test_one(self):
        generator = get_primes(1)
        self.assertEqual(generator.next(), 2)
        self.assertEqual(generator.next(), 3)
        self.assertEqual(generator.next(), 5)

    def test_one_hundred_one(self):
        generator = get_primes(101)
        self.assertEqual(generator.next(), 101)
        self.assertEqual(generator.next(), 103)
        self.assertEqual(generator.next(), 107)


class PrintSuccessivePrimesTestCase(TestCase):

    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out

    def test_one(self):
        print_successive_primes(5, start_number=1)
        output = self.out.getvalue().strip()
        self.assertIn('1: 2', output)
        self.assertIn('2: 3', output)
        self.assertIn('3: 5', output)
        self.assertIn('4: 7', output)
        self.assertIn('5: 11', output)

    def test_one_hundred_one(self):
        print_successive_primes(3, start_number=101)
        output = self.out.getvalue().strip()
        self.assertIn('1: 101', output)
        self.assertIn('2: 103', output)
        self.assertIn('3: 107', output)


if __name__ == '__main__':
    main()
