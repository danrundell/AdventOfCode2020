
class node(object):
    def __init__(self,v):
        self.value = v
        self.next = None
text = [int(x) for x in open('Day23/input.txt').read()]
minval = min(text)
maxval = max(text)
text += [x for x in range(maxval+1,1000001)]
maxval = 1000000
lookups = {}
cur = node(text[0])
lookups[text[0]] = cur
head = cur
for x in text[1:]:
    cur.next = node(x)
    cur = cur.next
    lookups[x] = cur
cur.next = head
for x in range(0,10000000):
    nextthreehead = head.next
    nextthree = [head.next.value, head.next.next.value, head.next.next.next.value]
    head.next = head.next.next.next.next
    label = head.value-1
    if label < minval:
        label = maxval
    while label in nextthree:
        label -= 1
        if label < minval:
            label = maxval
    searchcur = lookups[label]
    buf = searchcur.next
    searchcur.next = nextthreehead
    nextthreehead.next.next.next = buf
    head = head.next

print(lookups[1].next.value*lookups[1].next.next.value)