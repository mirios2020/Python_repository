def factorial(vul):
    if vul == 0:
        return(1)
    factorial = 1
    while vul > 0:
        factorial *= vul
        vul -= 1
    return(factorial)
def my_sum(x):
    e = 0.0001
    k = 1
    summa = 0
    while True:
        var = (((-1)**(k + 1))/(factorial((2*k))) * ((x / 3)**(4 * k)))
        summa += var
        if abs(var) < e:
            return(var, summa)
        k += 1
print(my_sum(5))