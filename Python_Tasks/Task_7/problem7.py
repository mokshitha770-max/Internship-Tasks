#Q7.Alphabet Rangoli

def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        letters = left + right
        line = "-".join(letters)
        lines.append(line.center(4 * size - 3, "-"))

    print("\n".join(lines + lines[-2::-1]))


n = int(input())
print_rangoli(n)
