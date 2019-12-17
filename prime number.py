# this program show prime numbers, up until 3000
import math

def isprime(n):
    if n in [0,1]:
        return False
    if (n>2) and (n%2==0):
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
        return True
prime = []
for i in range(3000):
    if isprime(i):
        prime.append(i)
print(prime)
