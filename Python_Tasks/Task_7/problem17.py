#Q17.Seperate the Numbers

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        parts = ""

        while len(parts) < len(s):
            parts += str(current)
            current += 1

        if parts == s:
            print("YES", first)
            return

    print("NO")

q = int(input())

for _ in range(q):
    separateNumbers(input().strip())
