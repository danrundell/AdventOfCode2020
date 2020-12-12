lines = [int(x) for x in open('Day10/input.txt').readlines()]

ones = 0
threes = 1
latest = 0
q = sorted(lines)
while (len(q) > 0):
    lowest = q[0]
    q = q[1:]
    if (lowest - latest) == 1:
        ones += 1
    elif (lowest - latest) == 3:
        threes += 1
    latest = lowest
print(ones*threes)