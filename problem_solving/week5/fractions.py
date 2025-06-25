#import Math
class Fraction():
    def __init__(self, num, denom):
        if(denom == 0 and num != 0):
            raise ZeroDivisionError
        if(num < 0 and denom < 0):
            self.numerator = num * -1
            self.denominator = denom * -1
        else:
            self.numerator = num
            self.denominator = denom        

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
    
    def __add__(self, frac2):
        if(self.denominator != frac2.get_denominator()):
            commonDenom = frac2.get_denominator() * self.denominator
            new_num1 = self.numerator * frac2.get_denominator()
            new_num2 = frac2.get_numerator() * self.denominator
            #print(f"{new_num1 + new_num2} / {commonDenom}")
            newFrac = Fraction(new_num1 + new_num2, commonDenom).reduce()
        else:
            #print(f"{self.numerator + frac2.get_numerator()} / {self.denominator}")
            newFrac = Fraction(self.numerator + frac2.get_numerator(), self.denominator).reduce()
        return newFrac
    
    def __sub__(self, frac2):
        if(self.denominator != frac2.get_denominator()):
            commonDenom = frac2.get_denominator() * self.denominator
            new_num1 = self.numerator * frac2.get_denominator()
            new_num2 = frac2.get_numerator() * self.denominator
            newFrac = Fraction(new_num1 - new_num2, commonDenom).reduce()
        else:
            newFrac = Fraction(self.numerator - frac2.get_numerator(), self.denominator).reduce()
        return newFrac

    def __mul__(self, frac2):
        newFrac = Fraction(self.numerator * frac2.get_numerator(), self.denominator * frac2.get_denominator()).reduce()
        return newFrac
    
    def __truediv__(self, frac2):
        newFrac = Fraction(self.numerator * frac2.get_denominator(), self.denominator * frac2.get_numerator()).reduce()
        return newFrac

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def reduce(self):
        if((self.numerator < 0 and self.denominator > 0) or (self.denominator < 0 and self.numerator > 0)): #Fraction is actually negative
            iterator = min(abs(self.numerator), abs(self.denominator))
            while(iterator >= 2):
                if(self.numerator % iterator == 0 and self.denominator % iterator == 0):
                    self.numerator = int(self.numerator / iterator)
                    self.denominator = int(self.denominator / iterator)
                    iterator = min(abs(self.numerator), abs(self.denominator))
                else:
                    iterator -= 1
        else:
            iterator = min(self.numerator, self.denominator)
            
            while(iterator >= 2):
                if(self.numerator % iterator == 0 and self.denominator % iterator == 0):
                    self.numerator = int(self.numerator / iterator)
                    self.denominator = int(self.denominator / iterator)
                    iterator = min(self.numerator, self.denominator)
                else:
                    iterator -= 1
        return self


if __name__ == "__main__":
    frac1 = Fraction(1, 2)
    frac2 = Fraction(10, 50)
    print(f"Frac1 = {frac1}\nFrac2 = {frac2}")
    print(f"{frac1} + {frac2} = {frac1+frac2}")
    print(f"{frac1} - {frac2} = {frac1-frac2}")
    print(f"{frac2} - {frac1} = {frac2-frac1}")
    print(f"{frac1} * {frac2} = {frac1*frac2}")
    print(f"{frac1} / {frac2} = {frac1/frac2}")


    