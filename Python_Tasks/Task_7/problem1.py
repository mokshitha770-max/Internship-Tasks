#Q1. Set .symmetric_difference() Operation

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english.symmetric_difference(french)))
