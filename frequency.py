
a = input("enter the string")
h = []
m = 1
p = []
d = {}
f = {}
for i in a:
    h.append(i)
h.sort()
x = set()
for j in h:
    x.add(j)
for k in x:
    d[k] = h.count(k)
y = sorted(d, key = d.get, reverse = True)
for i in y:
    f[i] = h.count(i)
    print(i, "=", h.count(i))
