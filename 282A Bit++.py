x = 0
number_of_statements = int(input())
for count in range(number_of_statements):
    statement = input()
    if statement == "X++" or statement == "++X":
        x += 1
    elif statement == "X--" or statement == "--X":
        x -= 1
print(x)