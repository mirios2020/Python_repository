s = '\t\t\t\tCALCULATION OF THE APPROXIMATE VALUE OF AN INFINITE SUM'
print(s)
n = int(input('Enter an integer: '))
e = float(input('Enter the calculation accuracy: \n E = '))
check = 0
k = 1
while k < n:
    var = ((-1) ** k) * (n / ((k + 1) * (k + 2))) ** k
    if abs(var) < e:
        check = 1
        print('E = ', var)
        break
    k = k + 1
if check is 0:
    print('I can\'t count with this approximation')
ex = input('Press to exit with application')
exit
