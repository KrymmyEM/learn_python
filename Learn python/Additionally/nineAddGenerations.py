import random
import itertools

def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min,max)

rand_sequence = randoms(0, 30, 15)
five_taken = list(itertools.islice(rand_sequence, 5))

print(five_taken)

seq = list(randoms(0, 30, 5))

def randomsInfinity(min, max):
    while True:
        yield random.randint(min,max)

rand_sequence = randomsInfinity(0, 9999)
taken = list(itertools.islice(rand_sequence, 50))
print(taken)
