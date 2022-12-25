a = int(input())
l = []
for i in range(a):
    k = int(input())
    l.append(k)
print(l)

for b in range(len(l)):
    for t in range(b + 1, len(l)):
        if l[b] >= l[t]:
            l[b], l[t] = l[t], l[b]

print(l)
