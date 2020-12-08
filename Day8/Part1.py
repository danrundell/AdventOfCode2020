lines = open('Day8/input.txt').readlines()
acc = 0
cur = 0
seen_lines = set()
while(True):
    if cur in seen_lines:
        print(acc)
        break
    seen_lines.add(cur)
    tok = lines[cur].replace('\n','').split(' ')
    if tok[0] == 'jmp':
        cur += int(tok[1])
    if tok[0] == 'acc':
        acc += int(tok[1])
        cur += 1
    if tok[0] == 'nop':
        cur += 1