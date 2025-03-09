def closestPrimes(left: int, right: int) -> list[int]:
    def closest_primes(left, right):
        if right < 2:
            return [-1, -1]
        
        # Step 1: Use Sieve of Eratosthenes to find primes up to 'right'
        sieve = [True] * (right + 1)
        sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:  # If i is prime
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        # Step 2: Collect prime numbers in the range [left, right]
        primes = [x for x in range(left, right + 1) if sieve[x]]

        # Step 3: Find the closest pair of primes
        if len(primes) < 2:
            return [-1, -1]  # Not enough primes

        min_gap = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair

    # Test cases
    print(closest_primes(10, 19))  # Output: [11, 13]
    print(closest_primes(4, 6))    # Output: [-1, -1]

