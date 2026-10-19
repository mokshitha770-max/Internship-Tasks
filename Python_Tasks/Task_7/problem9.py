#Q9.Beautiful Binary String

def beautifulBinaryString(b):
    return b.count("010")


n = int(input())
b = input().strip()
print(beautifulBinaryString(b))
