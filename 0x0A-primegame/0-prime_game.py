#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """
    Helper function to get list of primes up to a given number n
    using Sieve of Eratosthenes
    """

    def sieve(n):
        """
        computes all prime numbers up to the highest number n
        specified in the input, ensuring efficient prime retrieval.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    # Calculate primes once up to the maximum n in nums
    max_n = max(nums)
    primes = sieve(max_n)

    # Store the amount of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Process each round
    for n in nums:
        # Extract primes up to n
        current_primes = [p for p in primes if p <= n]

        # Determine the outcome based on the number of primes
        if len(current_primes) % 2 == 1:
            # If the number of primes is odd, Maria wins
            maria_wins += 1
        else:
            # If the number of primes is even, Ben wins
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
