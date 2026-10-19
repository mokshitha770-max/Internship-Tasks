#Q18.String Construction

def stringConstruction(s):
    return len(set(s))

q = int(input())

for _ in range(q):
    print(stringConstruction(input().strip()))
