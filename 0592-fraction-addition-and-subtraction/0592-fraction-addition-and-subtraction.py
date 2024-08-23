import math
from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        fractions = []
        i = 0
        n = len(expression)
        
        while i < n:
            if expression[i] in "+-":
                sign = expression[i]
                i += 1
            else:
                sign = "+"
            
            j = i
            while j < n and expression[j] not in "+-":
                j += 1
            
            frac = sign + expression[i:j]
            fractions.append(Fraction(frac))
            i = j
        
        result = sum(fractions)
        
        numerator = result.numerator
        denominator = result.denominator
        
        return "{}/{}".format(numerator, denominator)


        