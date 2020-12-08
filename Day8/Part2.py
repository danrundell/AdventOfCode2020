lines = open('Day8/input.txt').readlines()
accs = {}
curs = {}
should_run = True
while (should_run):
    for x in range(0, len(lines)):
        if x not in curs:
            curs[x] = 0
        if x not in accs:
            accs[x] = 0
        if curs[x] >= len(lines):
            print(accs[x])
            should_run = False
        tok = lines[curs[x]].replace('\n','').split(' ')
        if tok[0] == 'jmp':
            if curs[x] == x:
                curs[x] += 1
            else:
                curs[x] += int(tok[1])
        if tok[0] == 'acc':
            accs[x] += int(tok[1])
            curs[x] += 1
        if tok[0] == 'nop':
            if curs[x] == x:
                curs[x] += int(tok[1])
            else:
                curs[x] += 1
            