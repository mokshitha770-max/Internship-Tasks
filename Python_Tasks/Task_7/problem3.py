#Mars Exploration

def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(a != b for a, b in zip(s, expected))


s = input().strip()
print(marsExploration(s))
