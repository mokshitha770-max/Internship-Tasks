#Q20.Super Reduced String

def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack) if stack else "Empty String"

print(superReducedString(input().strip()))
