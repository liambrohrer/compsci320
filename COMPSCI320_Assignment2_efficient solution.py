import sys
import time
from collections import deque

start_time = time.time()
time.sleep(1)
#sys.stdin = open("COMPSCI320_Assignment2_input.txt", "r")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_key = left[i][1] + (100 - left[i][0])
        right_key = right[j][1] + (100 - right[j][0])

        if left_key >= right_key:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

while True:
    try:
        order = int(sys.stdin.readline().strip())
    except:
        break

    jobs = []
    total_lateness = 0
    jtime = 0

    for i in range(order):
        jobs.append(list(map(int, sys.stdin.readline().split())))

    q = deque(merge_sort(jobs))

    while q:
        if q[0][0] > jtime:
            q.popleft()
            jtime += 1
        else:
            late_job = q.popleft()
            total_lateness += late_job[1]
            late_job[1] = 0
            late_job[0] = 100
            q.append(late_job)

    print(total_lateness)

    end_time = time.time()  # record end time
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")