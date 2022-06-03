number = input()
colors = list(input())
count = 0
for x in range(len(colors)-1):
    if colors[x] == colors[x+1]:
        count += 1
print(count)
