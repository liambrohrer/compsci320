def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    result = None

    while row < m and col >= 0:
        val = matrix[row][col]
        if val == target:
            result = (row, col)
            col -= 1
        elif val > target:
            col -= 1
        else:
            row += 1
        if result and row > result[0]:
            break

    return result

def process_case(m, n, k, mat, queries):
    results = []
    for q in queries:
        res = search_matrix(mat, q)
        results.append(f"{res[0]} {res[1]}" if res else "None")
    return results


def main():
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    idx = 0
    output = []

    while idx < len(input_data):
        m, n, k = map(int, input_data[idx].split())
        idx += 1
        if m == 0 and n == 0 and k == 0:
            break

        mat = []
        for _ in range(m):
            row = list(map(int, input_data[idx].split()))
            mat.append(row)
            idx += 1

        queries = []
        for _ in range(k):
            queries.append(int(input_data[idx]))
            idx += 1

        output.extend(process_case(m, n, k, mat, queries))

    print("\n".join(output))


if __name__ == "__main__":
    main()