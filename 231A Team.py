number_of_probs = int(input())
number_of_solves = 0
for count in range(number_of_probs):
    x, y, z = list(map(int, input().split()))
    if (x+y+z) > 1:
        number_of_solves += 1
print(number_of_solves)
