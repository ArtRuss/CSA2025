import math

class Fraction():
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return self
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    def __add__(self, second):
        newDenom = math.lcm(self.denominator, second.denominator)
        firstScale = newDenom/self.denominator
        secondScale = newDenom/second.denominator
        newNum = int(self.numerator*firstScale) + int(second.numerator*secondScale)
        return Fraction(newNum, newDenom)
    def __sub__(self, second):
        newDenom = math.lcm(self.denominator, second.denominator)
        firstScale = newDenom/self.denominator
        secondScale = newDenom/second.denominator
        newNum = int(self.numerator*firstScale) - int(second.numerator*secondScale)
        return Fraction(newNum, newDenom)
    def __mul__(self, second):
        newNum = self.numerator * second.numerator
        newDenom = self.denominator * second.denominator
        return Fraction(newNum, newDenom)
    def __truediv__(self, second):
        newSecond = Fraction(second.denominator, second.numerator)
        newNum = self.numerator * newSecond.numerator
        newDenom = self.denominator * newSecond.denominator
        return Fraction(newNum, newDenom)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
# Test the Fraction class
if __name__ == "__main__":

    f1 = Fraction(2, 4)
    f2 = Fraction(1, 3)

    result = f1 + f2
    print(f"{f1} + {f2} = {result}")
    result = f1 - f2
    print(f"{f1} - {f2} = {result}")
    result = f1 * f2
    print(f"{f1} * {f2} = {result}")
    result = f1 / f2
    print(f"{f1} / {f2} = {result}")