# Solution to problem 5
# Rebecca Turley, 2019-02-18
# primes.py


n = int(input("Please enter a positive integer: "))


for x in range(2, n):
        if n % x == 0:
            print(n, 'is not a prime.')
            break
else:
        # loop fell through without finding a factor
        print(n, 'That is a prime.')
