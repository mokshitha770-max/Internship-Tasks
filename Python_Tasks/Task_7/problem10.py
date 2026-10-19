#Q10.Camel Case

s = input().strip()
words = 1

for ch in s:
    if ch.isupper():
        words += 1

print(words)
