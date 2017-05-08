import unittest
from primes import primes

class TestPrimes(unittest.TestCase):

	def test_primes_1(self):
		self.assertEqual(primes(5), [2,3,5])