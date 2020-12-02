lines = open('Day2/input.txt').readlines()
ct = 0
for line in lines:
    parts = line.split(' ')
    minl = int(parts[0].split('-')[0])
    maxl = int(parts[0].split('-')[1])
    required = parts[1][0]
    password = parts[2].replace('\n','')
    if password[minl-1] == required and password[maxl-1] != required:
        ct += 1
    elif password[minl-1] != required and password[maxl-1] == required:
        ct += 1
print(ct)