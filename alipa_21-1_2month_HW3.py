import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, other):
        nod = math.gcd(self.denominator, other.denominator)
        znam = self.denominator * other.denominator // nod
        chisl = znam // self.denominator * self.numerator + znam //other.denominator * other.numerator
        return f"{chisl}/{znam}"

    def __sub__(self, other):
        nod = math.gcd(self.denominator, other.denominator)
        znam = self.denominator * other.denominator // nod
        chisl = znam // self.denominator * self.numerator - znam //other.denominator * other.numerator
        return f"{chisl}/{znam}"

    def __mul__(self, other):
        # nod = math.gcd(self.denominator, other.denominator)
        znam = self.denominator * other.denominator
        chisl = self.numerator * other.numerator
        return f"{chisl}/{znam}"

    def __floordiv__(self, other):
        znam = self.denominator * other.numerator
        chisl = self.numerator * other.denominator
        return f"{chisl}/{znam}"



