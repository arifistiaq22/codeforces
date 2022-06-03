ages = list(map(int,input().split()))
years = 0
for x in range(100):
    ages[0] *= 3
    ages[1] *= 2
    years += 1
    if ages[0] > ages[1]:
        break
print(years)