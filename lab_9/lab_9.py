n = int(input('Enter the number of members of the sum: '))
a = []
x = 2

i = 0
while i < n:
    print('Enter the term member a', i, ': ')
    vul = int(input())
    a.append(vul)
    i += 1
print(a)
P = a[0] + a[1] * x
i = 2
while i < n:
    var = a[i] * x**a[i]
    P += var
    i += 1
print(P)
