class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def _gcd(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    
    def simplify(self):
        the_gdc = self._gcd()
        self.numerator = self.numerator//the_gdc
        self.denominator = self.denominator//the_gdc
    
    def __add__(self, other):
        numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result
    
    def __sub__(self, other):
        numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __pow__(self, other):
        numerator = (self.numerator ** (1/other.denominator))
        denominator = (self.denominator ** (1/other.denominator))
        return Fraction(numerator ** other.numerator, denominator ** other.numerator)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

fraction1_input = input("Whats the numerator and denominator (enter a list): ").split()
fraction2_input = input ("Whats the second numerator and denominator (enter a list): ").split()

fraction1 = Fraction(int(fraction1_input[0]), int(fraction1_input[1]))
fraction2 = Fraction(int(fraction2_input[0]), int(fraction2_input[1]))
fraction3 = fraction1 + fraction2
print(fraction3)

        