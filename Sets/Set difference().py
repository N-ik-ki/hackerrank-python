n = input()
eng = set(map(int, input().split()))
b = input()
frn = set(map(int, input().split()))
print(len(eng.difference(frn)))
