prime_numbers = [n for n in range(2, 1000) if all([n % i for i in range(2, n)])]
