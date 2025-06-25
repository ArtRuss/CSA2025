# June 25, 2025
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            while numerator - int(numerator) > 0 or denominator - int(denominator) > 0:
                numerator *= 10
                denominator *= 10
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.reduce()

    def to_float(self):
        return self.numerator / self.denominator

    def reduce(self):
        """ (Mutating function) reduce fraction by finding gcd of numerator and denominator """
        divisor = gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor
        if (self.denominator < 0):
            self.numerator *= -1
            self.denominator *= -1

    def reduced(self):
        """ (Non-mutating function) reduce fraction by finding gcd of numerator and denominator """
        divisor = gcd(self.numerator, self.denominator)
        n = self.numerator // divisor
        d = self.denominator // divisor
        if (d < 0):
            n *= -1
            d *= -1
        return Fraction(n, d)

    def inverted(self):
        n = self.denominator
        d = self.numerator
        if (d < 0):
            n *= -1
            d *= -1
        return Fraction(n, d)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        out = Fraction(numerator, denominator)
        return out.reduced()

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        out = Fraction(numerator, denominator)
        return out.reduced()

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self + (-other)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self * other.inverted()

    def __pow__(self, exponent):
        n = self.numerator ** exponent
        d = self.denominator ** exponent
        out = Fraction(n, d)
        return out.reduced()

    def __repr__(self):
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

    def __str__(self):
        return f"({self.numerator}/{self.denominator})"

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return other * self.inverted()

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

if __name__ == "__main__":
    half = Fraction(1,2)
    print(float(5.2 * half))
    print(int(50 / half))
    print(int(50 * half))
    print(0.5 + half)
    print(float(50 + half))
    quarter = Fraction(1,4)
    print(half*quarter)
    print(half-quarter**2)
    print(Fraction(1/2) / 0.5)
    # we set denominator to 1 by default :)
    print(Fraction(4.3)**2)
    print(Fraction(23/2))
