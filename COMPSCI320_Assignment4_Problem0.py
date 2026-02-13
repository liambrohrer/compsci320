import sys

def problem0(S1, S2):
    n1 = len(S1)
    for x in S2:
        print(n1 + x)

if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()
    
    S1 = list(map(int, lines[0].split()))
    S2 = list(map(int, lines[1].split()))
    
    problem0(S1, S2)