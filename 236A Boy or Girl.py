name = list(input())
distinct = [0]
for count in range(len(name)):
    has = 0
    for x in range(len(distinct)):
        if name[count] == distinct[x]:
            has += 1
    if has == 0:
        distinct += name[count]
print("CHAT WITH HER!") if (len(distinct)-1) % 2 == 0 else print("IGNORE HIM!")