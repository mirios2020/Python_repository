import re
data = [
    ['D11', 'D21', 'D31', 'D22', 'D41', '23', 'D32', 'D25'],
    [20,     10,    15,    30,    25,    6,    22,    30]
]
result = 0
iteration = 0
while iteration < 8:
    if re.match(r'D2\w', data[0][iteration]):
        if data[1][iteration] > 15:
            result += data[1][iteration]
    iteration += 1
print (result)