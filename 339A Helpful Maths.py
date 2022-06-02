from os import sep


numbers = sorted(list(map(int, input().split(sep = "+"))))
final = str()
for x in range(len(numbers)-1):
    final = final + str(numbers[x]) + "+"
print(final+str(numbers[-1]))