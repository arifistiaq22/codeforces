banana = list(map(int, input().split()))
cost = 0
for x in range(banana[2]):
    cost = cost + (x+1)*banana[0]
print(cost-banana[1]) if (cost-banana[1]) > 0 else print(0)