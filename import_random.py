import random

# random floating point numbers #
for _ in range(5):
    print(random.random(), end=' ')  # gives floating point value between 0(included) and 1(excluded)
print()
for _ in range(5):
    print(random.uniform(1, 3), end=' ')  # gives floating point value between 'i' and 'j' both included
print()
print("------------------------------------------------------------------------")

# random integers #
for _ in range(25):
    print(random.randint(1, 3), end=' ')  # randint(i, j) gives integer values between 'i' and 'j' both inclusive
print()
for _ in range(25):
    print(random.randrange(1, 3), end=' ')  # randrange(i, j) gives integer values between 'i'(included) and 'j'(excluded)
print()
for _ in range(25):
    print(random.randrange(6, 4, -1), end=' ')  # randrange(i, j, step)
print()
print("------------------------------------------------------------------------")

# random items from list #
colors = ["red", "blue", "green", "yellow"]
for _ in range(5): print(random.choice(colors), end='\t')
print()
print(random.choices(colors, k=5))  # returns a list of 'k' items
print(random.choices(colors, weights=[4,2,0,8], k=5))
print(random.sample(colors, k=3)) # sample() doesn't have keyword argument 'weights' # returns a list of unique values
print("------------------------------------------------------------------------")

# shuffle #
random.shuffle(colors)  # shuffles the items of list:'colors' and returns 'None'
print(colors)
print("------------------------------------------------------------------------")

# SEED #
# The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value), to be able to generate a random number.
# # By default the random number generator uses the current system time.

[print(random.random(), "\t", random.randint(1, 1000), end='\t') for _ in range(3)]
print()

# Use the seed() method to customize the start number of the random number generator.
# # Note: If you use the same seed value twice you will get the same random number twice.
for _ in range(3):
    random.seed(10)
    [print(random.random(), "\t", random.randint(1, 1000), end='\t') for _ in range(3)]
    print()

# Observe following two values: y[i] = 1000 * x[i]
random.seed(0)
x = [random.random() for _ in range(3)]
print(x)
random.seed(0)
y = [random.uniform(0, 1000) for _ in range(3)]
print(y)
print("------------------------------------------------------------------------")
