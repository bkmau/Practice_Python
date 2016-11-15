import unittest

class PrimeFactor:
    def get_prime_factor(self, n):
        factors = []
        if n > 1:
            candidate = 2
            while candidate <= n:
                if ((n % candidate) == 0):
                    if not candidate in factors:
                        factors.append(candidate)
                    n /= candidate
                else:
                    candidate += 1
        return factors

class PrimeFactorTest(unittest.TestCase):
    def setUp(self):
        self.factors = PrimeFactor()

    def test_OneIsNotAPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(1), [])

    def test_TwoIsAPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(2), [2])

    def test_FourHasTwoAsItsPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(4), [2])

    def test_ThreeIsAPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(3), [3])

    def test_FiveIsAPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(5), [5])

    def test_SixHasTwoPrimeFactor(self):
        self.assertEquals(self.factors.get_prime_factor(6), [2, 3])

    def test_BigNumber(self):
        self.assertEquals(self.factors.get_prime_factor(23412), [2, 3, 1951])

if __name__ == '__main__':
    unittest.main()
