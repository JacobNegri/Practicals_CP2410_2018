# Jacob Negri
#S:N 13165429

def count_nodes(L):
    if L.current is None:
        return 0
    count = 1
    original = L.current
    current = original

    while current.next != original:
        count += 1
    return count
