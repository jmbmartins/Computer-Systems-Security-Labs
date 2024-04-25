import sys
import getopt

def bit_length(self):
   """This function returns the number of bits of self"""
   s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
   s = s.lstrip('-0b') # remove leading zeros and minus sign
   return len(s)       # len('100101') --> 6

def inv(n):
    for i in range(p):
        if (n * i) % p == 1:
            return i

def extended_gcd(aa, bb):
   lastremainder, remainder = abs(aa), abs(bb)
   x, lastx, y, lasty = 0, 1, 1, 0
   while remainder:
       lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
       x, lastx = lastx - quotient*x, x
       y, lasty = lasty - quotient*y, y
   return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modInverse(a, n):
   """This function calculates the inverse of a modulo n"""
   g, x, y = extended_gcd(a, n)
   if g != 1:
       raise ValueError
   return x % n

class ECcurve:
   """A class defining a curve for elliptic curve crypto"""
   p = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF", 16)
   a = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFC", 16)
   b = int("64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1", 16)
   n = int("FFFFFFFFFFFFFFFFFFFFFFFF99DEF836146BC9B1B4D22831", 16)
   h = int("01", 16)
   fieldSize = 192

class ECPoint:
   """A class defining a point for the EC"""
   x = 0
   y = 0
   ec = ECcurve()

   def __init__(self, x, y):
      self.x = x
      self.y = y


   def doublePoint(self):
      s = ((3 * (self.x * self.x)) + self.ec.a ) * (modInverse(2 * self.y, self.ec.p)) % self.ec.p
      x3 = (s * s - self.x - self.x) % self.ec.p
      y3 = (s * (self.x - x3) - self.y) % self.ec.p
     
      return ECPoint(x3,y3)

   def sum(self,p2):
     
     #CODE IS MISSING   
     
     x3 = 0
     y3 = 0
     return ECPoint(x3,y3)


   def multiplyPointByScalar(self, n):
     
     result = ECPoint(self.x,self.y)
     p1 = ECPoint(self.x,self.y)

     #CODE IS MISSING

     return result;



def main():
  p1 = ECPoint(int("188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012",16),int("07192B95FFC8DA78631011ED6B24CDD573F977A11E794811", 16))
  print(hex(int(p1.doublePoint().x)))
  print(hex(int(p1.doublePoint().y)))
  p2 = p1.doublePoint()
  p3 = p2.sum(p1)


  print("p1+p1+p1")
  print(hex(int(p2.sum(p1).x)))
  print(hex(int(p2.sum(p1).y)))

  print("3*p1")
  print(hex(int(p1.multiplyPointByScalar(3).x)))
  print(hex(int(p1.multiplyPointByScalar(3).y)))

  print("p1+p1+p1+p1")
  print(hex(int(p3.sum(p1).x)))
  print(hex(int(p3.sum(p1).y)))
