s = []
k = int(input("Enter the fibonacci series end:"))
a = 0
j = 3
for i in range(0, k):
    if i<2:
        s += [i]
    elif i >= 2:
        a = s[i-1]+s[i-2]
        s.append(a)
        print(s)
