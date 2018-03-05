# Practical 1
# Task 3

# Name: Jacob Negri
# S:N: 13165429

seq = [2, 4, 7, 33]

def distinct_num(seq):
    for i in range(0, len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j]:
                return False
    return True

#Testing function works
print(distinct_num(seq))