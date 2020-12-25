doorKey = 12232269
cardKey = 19452773

subjectValue = 7
doorLoopSize = 0
doorValue = 1

while(True):
    doorLoopSize += 1
    doorValue *= subjectValue
    doorValue = doorValue % 20201227
    if doorValue == doorKey:
        break


cardLoopSize = 0
cardValue = 1
while(True):
    cardLoopSize += 1
    cardValue *= subjectValue
    cardValue = cardValue % 20201227
    if cardValue == cardKey:
        break
print(f'door: {doorLoopSize}, card: {cardLoopSize}')

subjectValue = doorKey
sharedKeyValue = 1
for x in range(0,cardLoopSize):
    sharedKeyValue *= subjectValue
    sharedKeyValue = sharedKeyValue % 20201227

print(sharedKeyValue)
