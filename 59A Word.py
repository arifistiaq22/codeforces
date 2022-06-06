word = input()
main_word = list(word)
upp = list(word.upper())
down = list(word.lower())
a = b = 0
for x in range(len(main_word)):
    if main_word[x] == upp[x]:
        a += 1
    elif main_word[x] == down[x]:
        b += 1
if b >= a:
    print(''.join(down))
else:
    print(''.join(upp))