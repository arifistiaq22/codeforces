from re import S


count = int(input())
results = [None] * count
for x in range(count):
    words = input()
    if (len(words) <= 10):
        results[x] = words
    else:
        results[x] = words[0] + str(len(words)-2) + words[-1]
for x in range(count):
    print(results[x])

