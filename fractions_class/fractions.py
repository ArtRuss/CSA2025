class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __add__(self, other):
        numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __sub__(self, other):
        numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
fraction1 = Fraction(1,2)
fraction2 = Fraction(1,4)
fraction3 = fraction1 - fraction2
print(fraction3)

        