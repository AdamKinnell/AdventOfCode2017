from math import sqrt, floor

def is_prime(x):
    for i in range(2, floor(sqrt(x))):
        if x % i == 0:
            return False
    return True

composites = 0
numbers = range(107_900, 124_900 + 1, 17)
for n in numbers:
    if not is_prime(n):
        composites += 1

print('Number of composites:', composites) # = 907
