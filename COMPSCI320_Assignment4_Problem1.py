import sys

def binary_search(S1, x):
    lo, hi = 0, len(S1) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if S1[mid] == x:
            result = mid
            lo = mid + 1
        elif S1[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

def problem1(S1, S2):
    for x in S2:
        print(binary_search(S1, x))

if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()
    
    S1 = list(map(int, lines[0].split()))
    S2 = list(map(int, lines[1].split()))
    
    problem1(S1, S2)