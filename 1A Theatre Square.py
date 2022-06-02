n, m, a = list(map(int, input().split()))
if n%a == 0:
    row = n/a
else:
    row = int(n/a)+1
if m%a == 0:
    col = m/a
else:
    col = int(m/a)+1
print(int(row*col))