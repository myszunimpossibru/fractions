from math import gcd

class Fraction(object):


    denominator = None
    nominator = None

    
    def __init__(self, nominator, denominator):



        self.nominator = nominator
        self.denominator = denominator
        



        if self.denominator == 0:
            raise ValueError("denominator must not be zero.")
        

        divisor = gcd(self.nominator, self.denominator)


        self.nominator = int(nominator//divisor)
        self.denominator = int(denominator//divisor)
        
        if (self.denominator < 0):
            self.denominator = -1 * self.denominator
            self.nominator = -1 * self.nominator

    def __str__(self):
        if self.denominator == 1:
            return "{0.nominator}".format(self)
        else:
            return "{0.nominator}/{0.denominator}".format(self)
    
    def __mul__(self, number):
        return Fraction(self.nominator * number.nominator, self.denominator * number.denominator)
    
    def __truediv__(self, number):
        return Fraction(self.nominator * number.denominator, self.denominator * number.nominator)
    
    def __add__(self, number):
        n1 = self.nominator * number.denominator
        n2 = self.denominator * number.nominator
        return Fraction(n1 + n2, self.denominator * number.denominator)
    
    def __sub__(self, number):
        n1 = self.nominator * number.denominator
        n2 = self.denominator * number.nominator
        return Fraction(n1 - n2, self.denominator * number.denominator)

    def __eq__(self, number):
        return self.nominator == number.nominator and self.denominator == number.denominator

    def value(self):
        return self.nominator/self.denominator
		