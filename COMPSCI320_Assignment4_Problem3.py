import sys

def jewel_choice(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    p2 = arr[0]
    p1 = max(arr[0], arr[1])
    for i in range(2, n):
        curr = max(p1, arr[i] + p2)
        p2, p1 = p1, curr
    return p1

def max_circular(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    exclude_last = jewel_choice(arr[:-1])
    exclude_first = jewel_choice(arr[1:])
    return max(exclude_last, exclude_first)

def process_necklaces():
    for line in sys.stdin:
        line = line.strip()
        jewels = list(map(int, line.split()))
        total = sum(jewels)
        d1 = max_circular(jewels)
        d2 = total - d1
        print(d1, d2)

if __name__ == "__main__":
    process_necklaces()