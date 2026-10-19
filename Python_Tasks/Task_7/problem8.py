#Q8.Gemstones

n = int(input())
common = set(input().strip())

for _ in range(n - 1):
    common &= set(input().strip())

print(len(common))
