words = [input().lower(), input().lower()]
original = words
words = sorted(words)
if words[0] == words[1]:
    print(0)
elif words[0] == original[0]:
    print(-1)
else:
    print(1)