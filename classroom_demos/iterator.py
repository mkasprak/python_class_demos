# working with prime numbers
# 🤖

class PrimeIterator:
    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        while not self.is_prime(self.number):
            self.number += 1
        if self.number >= self.max:
            raise StopIteration
        return self.number

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# Example usage
for prime in PrimeIterator(25):
    print(prime)
