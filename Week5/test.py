import math
class Fraction():
    def __init__(self, numer, denom):

        self.numer = numer
        self.denom = denom

        if self.denom == 0:
            print("nonzero denominator only!")
            raise ValueError

        if isinstance(self.numer, int) and isinstance(self.denom, int):
            gcd = math.gcd(self.numer, self.denom)
            self.numer /= gcd
            self.denom /= gcd

            self.numer = int(self.numer)
            self.denom = int(self.denom)

        else:
            print("rational: int/int only!")
            raise TypeError

    def __add__(self, frac2):
        numer = (self.numer*frac2.denom) + (self.denom*frac2.numer)
        denom = self.denom * frac2.denom

        gcd = math.gcd(self.numer, self.denom)

        numer //= gcd
        denom //= gcd
        return Fraction(numer, denom)

    def __mul__(self, frac2):
        numer = self.numer*frac2.numer
        denom = self.denom*frac2.denom

        gcd = math.gcd(numer, denom)
        numer //= gcd
        denom //= gcd
        return Fraction(numer, denom)

    def __sub__(self, frac2):
        numer =(self.numer*frac2.denom) - (self.denom*frac2.numer)
        denom = self.denom * frac2.denom

        gcd = math.gcd(self.numer, self.denom)
        numer //= gcd
        denom //= gcd
        return Fraction(numer, denom)

    def __truediv__(self, frac2):
        if frac2.numer == 0:
            print("nonzero denominator only!")
            raise ValueError

        numer = self.numer*frac2.denom
        denom = self.denom*frac2.numer

        gcd = math.gcd(self.numer, self.denom)
        numer //= gcd
        denom //= gcd
        return Fraction(numer, denom)

    def __str__(self):
        if self.denom != 1:
            return str(int(self.numer)) + " / " + str(int(self.denom))
        else:
            return str(self.numer) + ' (Also ' + str(self.numer) + " / " + str(self.denom) + ')'




if __name__ == "__main__":
    frac1 = Fraction(3,2)
    frac2 = Fraction(2,3)
    
    frac3 = frac1 + frac2
    frac4 = Fraction(0,1)
    print(frac3)
    print(frac2/frac1)
    print(frac1*frac2)
    print(frac2*frac1)
    print(frac1-frac2)
    print(frac2-frac1)
    print(frac1 * frac4)
