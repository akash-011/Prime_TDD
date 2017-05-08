import unittest
from primes import primes

class TestPrimes(unittest.TestCase):

	def test_primes_1(self):
		self.assertEqual(primes(5), [2,3,5])
	def test_primes_2(self):
		self.assertEqual(primes(20), [2,3,5,7,11,13,17,19])
