#Q13.Sherlock and the valid string

from collections import Counter

def isValid(s):
    freq = list(Counter(s).values())
    counts = Counter(freq)

    if len(counts) == 1:
        return "YES"

    if len(counts) != 2:
        return "NO"

    (f1, c1), (f2, c2) = counts.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
        return "YES"

    return "NO"

print(isValid(input().strip()))
