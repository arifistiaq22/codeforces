numbers = list(map(int, input().split()))
for x in range(numbers[1]):
    if numbers[0] % 10 != 0:
        numbers[0] -= 1
    else:
        numbers[0] = numbers[0]/10
print(int(numbers[0]))