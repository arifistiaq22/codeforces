n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
qualified = 0
for count in range(n):
    if numbers[count] >= numbers[k-1] and numbers[count] != 0:
        qualified += 1
print(qualified)