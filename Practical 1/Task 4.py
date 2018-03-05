# Practical 1
# Task 4

# Name: Jacob Negri
# S:N: 13165429

#changing the harmonic function to a harmonic generator

def harmonic_gen(n):
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
        yield h