class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n # making a list of lenght n. And keep all the values as True.
        primes[0] = primes[1] = False #cause 0 , 1 not primes
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])# if we have mutiple of a number in the range of n, we have to remove them as they can be prime. i.e 2 is prime, but its multiple in n = 10 are 4,6,8 they cant be prime. So we will make them false(means not a prime)
        return sum(primes)


