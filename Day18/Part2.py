text = open('Day18/input.txt').readlines()
sums = 0
def collapseTree(tree):
    treecopy = [x for x in tree]
    treebuf = []
    while len(treecopy) > 0:
        top = treecopy[0]
        if len(treebuf) > 0 and treebuf[-1] == '+':
            treebuf.pop()
            treebuf.append(int(treebuf.pop())+int(top))
        else:
            treebuf.append(top)
        treecopy = treecopy[1:]
    treebuf = treebuf[::-1]
    treecopy = [x for x in treebuf]
    treebuf = []
    while len(treecopy) > 0:
        top = treecopy[0]
        if len(treebuf) > 0 and treebuf[-1] == '*':
            treebuf.pop()
            treebuf.append(int(treebuf.pop())*int(top))
        else:
            treebuf.append(top)
        treecopy = treecopy[1:]
    return treebuf[0]
for line in text:
    line = line.replace(' ','').replace('\n','')
    buf = []
    while len(line) > 0:
        if len(buf) == 0:
            buf.append(line[0])
        elif buf[-1] == '+' and (isinstance(line[0], int) or line[0].isdigit()):
            buf.pop()
            param = buf.pop()
            buf.append(int(param)+int(line[0]))
        elif buf[-1] == '*' and (isinstance(line[0], int) or line[0].isdigit()):
            buf.append(line[0])
        elif line[0] == '(':
            buf.append(line[0])
        elif line[0] == ')':
            subline = []
            while buf[-1] != '(':
                subline.append(buf.pop())
            subline = subline[::-1]
            buf.pop()
            collapsed = collapseTree(subline)
            if len(buf) > 0 and buf[-1] == '+':
                buf.pop()
                buf.append(collapsed+int(buf.pop()))
            else:
                buf.append(collapsed)
        else:
            buf.append(line[0])
        line = line[1:]
    bufcopy = [x for x in buf]
    bufcopy = bufcopy[::-1]
    buf = []
    while len(bufcopy) > 0:
        if len(buf) == 0:
            buf.append(bufcopy[0])
        elif buf[-1] == '*' and (isinstance(bufcopy[0], int) or bufcopy[0].isdigit()):
            buf.pop()
            param = buf.pop()
            buf.append(int(param)*int(bufcopy[0]))
        elif bufcopy[0] == '(':
            buf.append(bufcopy[0])
        elif bufcopy[0] == ')':
            subline = []
            while buf[-1] != '(':
                subline.append(buf.pop())
            subline = subline[::-1]
            buf.pop()
            buf.append(collapseTree(subline))
            if len(buf) > 0 and buf[-1] == '*':
                buf.pop()
                buf.append(collapsed*int(buf.pop()))
            else:
                buf.append(collapsed)
        else:
            buf.append(bufcopy[0])
        bufcopy = bufcopy[1:]
    sums += buf[0]
print(sums)
