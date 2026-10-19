#Q16.caesar cipher

def caesarCipher(s, k):
    result = []
    k %= 26

    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - 97 + k) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - 65 + k) % 26 + 65))
        else:
            result.append(ch)

    return ''.join(result)

n = int(input())
s = input().strip()
k = int(input())

print(caesarCipher(s, k))
