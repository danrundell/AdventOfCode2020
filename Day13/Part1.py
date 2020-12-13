text = open('Day13/input.txt').readlines()
timestamp = int(text[0])
schedules = text[1].replace('\n','').split(',')
closestTime = -1
closestBus = -1
for bus in schedules:
    if bus == 'x':
        continue
    elapsed = timestamp % int(bus)
    remaining = int(bus)-elapsed
    if remaining < closestTime or closestTime == -1:
        closestTime = remaining
        closestBus = int(bus)
print(closestBus*closestTime)