class Rational_fractions:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:  
            raise ZeroDivisionError('низя ноль пихать в знаменатель')
        self.denominator = denominator

    def Gcd_Evclid(self, num, denom):
        if num<0: num*= -1
        while num!=0 and denom!=0:
            if num>denom:
                num %= denom
            else:
                denom%=num
        print(num+denom)
        return num+denom

    def __add__(self, another_fraction):
        if self.denominator == another_fraction.denominator:
            self.numerator = self.numerator+another_fraction.numerator
        else:
            self.numerator = self.numerator*another_fraction.denominator+self.denominator*another_fraction.numerator  
            self.denominator *= another_fraction.denominator
            gcd = self.Gcd_Evclid(self.numerator, self.denominator)
            self.numerator = self.numerator//gcd
            self.denominator = self.denominator//gcd

    def __mull__(self, another_fraction):
        if self.denominator == another_fraction.denominator:
            self.numerator = self.numerator-another_fraction.numerator
        else:
            self.numerator = self.numerator*another_fraction.denominator-self.denominator*another_fraction.numerator  
            self.denominator *= another_fraction.denominator
            gcd = self.Gcd_Evclid(self.numerator, self.denominator)
            self.numerator = self.numerator//gcd
            self.denominator = self.denominator//gcd
     
    def __sub__(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        gcd = self.Gcd_Evclid(self.numerator, self.denominator)
        self.numerator = self.numerator//gcd
        self.denominator = self.denominator//gcd

    def __truediv__(self, other):
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        gcd = self.Gcd_Evclid(self.numerator, self.denominator)
        self.numerator = self.numerator//gcd
        self.denominator = self.denominator//gcd
    
        
    
             

