class node(object):
    def __init__(self,v):
        self.value = v
        self.next = None

text = [int(x) for x in open('Day23/input.txt').read()]
minval = min(text)
maxval = max(text)
lookups = {}
cur = node(text[0])
lookups[text[0]] = cur
head = cur
for x in text[1:]:
    cur.next = node(x)
    cur = cur.next
    lookups[x] = cur

cur.next = head

for x in range(0,100):
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


printhead = head    
buf = ''
while head.value != 1:
    head = head.next

head = head.next
while head.value != 1:
    buf += str(head.value)
    head = head.next

print(buf)