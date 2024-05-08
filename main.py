import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(self.numerator, "/", self.denominator)
    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def add(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.simplify()
        return self
    
    def main():
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        print(f"Fraction 1: {f1}")
        print(f"Fraction 2: {f2}")
        print("Sum of fractions:")
        result = f1.add(f2)
        result.show()
    if __name__ == "__main__":
        main()