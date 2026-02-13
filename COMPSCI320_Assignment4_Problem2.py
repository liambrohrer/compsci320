import sys

def find_pivot(S):
    n = len(S)
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if S[mid] > S[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo

def rotated_last_index(S, x):
    n = len(S)
    if n == 0:
        return -1

    p = find_pivot(S)
    seg1_len = n - p

    def get(i_unrot):
        return S[(i_unrot + p) % n]
    
    lo, hi = 0, n - 1
    left = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = get(mid)
        if val < x:
            lo = mid + 1
        elif val > x:
            hi = mid - 1
        else:
            left = mid
            hi = mid - 1

    if left == -1:
        return -1

    lo, hi = 0, n - 1
    right = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = get(mid)
        if val < x:
            lo = mid + 1
        elif val > x:
            hi = mid - 1
        else:
            right = mid
            lo = mid + 1

    if left <= seg1_len - 1:
        unrot_right_seg1 = min(right, seg1_len - 1)
        if unrot_right_seg1 >= left:
            return unrot_right_seg1 + p
        else:
            return (right + p) % n
    else:
        return (right + p) % n

def problem2(S1, S2):
    for x in S2:
        print(rotated_last_index(S1, x))

if __name__ == "__main__":
    data = sys.stdin.read().strip().splitlines()

    S1 = list(map(int, data[0].split()))
    S2 = list(map(int, data[1].split()))

    problem2(S1, S2)