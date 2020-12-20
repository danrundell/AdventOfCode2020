text = open('Day18/input.txt').readlines()
sums = 0
for line in text:
    line = line.replace(' ','').replace('\n','')
    buf = []
    while len(line) > 0:
        if len(buf) == 0:
            buf.append(line[0])
        elif buf[-1] == '+' and line[0].isdigit():
            buf.pop()
            param = buf.pop()
            buf.append(int(param)+int(line[0]))
        elif buf[-1] == '*' and line[0].isdigit():
            buf.pop()
            param = buf.pop()
            buf.append(int(param)*int(line[0]))
        elif line[0] == '(':
            buf.append(line[0])
        elif line[0] == ')':
            
            subbuf = []
            while buf[-1] != '(':
                subbuf.append(buf.pop())
            subbuf = subbuf[::-1]
            cur = 0
            while len(subbuf) > 0:
                if subbuf[-1] == '+':
                    subbuf.pop()
                    param = subbuf.pop()
                    subbuf.append(int(param)+cur)
                elif subbuf[-1] == '*':
                    subbuf.pop()
                    param = subbuf.pop()
                    subbuf.append(int(param)*cur)
                else:
                    cur = int(subbuf.pop())
            buf.pop()
            if len(buf) > 0 and buf[-1] == '+':
                buf.pop()
                buf.append(cur+int(buf.pop()))
            elif len(buf) > 0 and buf[-1] == '*':
                buf.pop()
                buf.append(cur*int(buf.pop()))
            else:
                buf.append(cur)
        else:
            buf.append(line[0])
        line = line[1:]
    sums += buf[0]
print(sums)