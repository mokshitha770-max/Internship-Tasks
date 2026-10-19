#Q6.Pangrams

def pangrams(s):
    letters = set(s.lower())

    if all(ch in letters for ch in "abcdefghijklmnopqrstuvwxyz"):
        return "pangram"

    return "not pangram"


s = input()
print(pangrams(s))
