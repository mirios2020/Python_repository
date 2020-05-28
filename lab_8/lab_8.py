file1 = 'file_T1.txt'
file2 = 'file_T2.txt'

f0 = open(file2, 'w')
f0.close()

key = ';'
str = ''
f1 = open(file1, 'r')

while True:
    char = f1.read(1)
    if not char:
        break
    str += char
    if char == key:
        f2 = open(file2, 'a')
        f2.write(str + '\n')
        f2.close()
        str = ''
    elif len(str) == 30:
        f2 = open (file2, 'a')
        f2.write(str + '\n')
        f2.close()
        str = ''

f1.close()
print('work with the file was successful. please check the file "file_T2" in the project folder')