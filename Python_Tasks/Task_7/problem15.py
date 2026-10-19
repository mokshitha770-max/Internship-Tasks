#Q15.Game of thrones_1

from collections import Counter

def gameOfThrones(s):
    odd = sum(1 for count in Counter(s).values() if count % 2)
    return "YES" if odd <= 1 else "NO"

print(gameOfThrones(input().strip()))
