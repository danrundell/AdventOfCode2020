text = open('Day13/input.txt').readlines()
#text[1] = '17,x,13,19'
scheduleLines = text[1].replace('\n','').split(',')

counter = 0
schedules = []
for x in scheduleLines:
    if x != 'x':
        schedules.append((int(x),counter))
    counter += 1
scheduleDeltas = [x[0] for x in schedules]

def findLcm(a):
    from math import gcd
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

step = 1
t = schedules[0][0]
mostMatches = 0
while(True):
    matches = []
    for x in range(0,len(schedules)):
        if ((t+schedules[x][1])%schedules[x][0]) == 0:
            matches.append(schedules[x][0])
    matches = list(set(matches))
    if len(matches) > 0 and len(matches) > mostMatches:
        step = findLcm(matches)
        mostMatches = len(matches)
    if len(matches) == len(schedules):
        print(t)
        break
    t += step

