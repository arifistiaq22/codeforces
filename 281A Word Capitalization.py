word = list(input())
first = word[0]
first = first.capitalize()
for count in range(len(word)-1):
    first = first + word[count+1]
print(first)