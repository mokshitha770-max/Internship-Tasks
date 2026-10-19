#Q19.Weighted Uniform Strings

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    count = 0

    for ch in s:
        if ch == previous:
            count += 1
        else:
            previous = ch
            count = 1

        weights.add((ord(ch) - ord('a') + 1) * count)

    for q in queries:
        print("Yes" if q in weights else "No")

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weightedUniformStrings(s, queries)
