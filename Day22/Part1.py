text = open('Day22/input.txt').read().split('\n\n')
player1 = [int(x) for x in text[0].strip().split('\n')[1:]]
player2 = [int(x) for x in text[1].strip().split('\n')[1:]]

while len(player1) > 0 and len(player2) > 0:
    top1 = player1[0]
    top2 = player2[0]
    player1 = player1[1:]
    player2 = player2[1:]
    if top1 > top2:
        player1.append(top1)
        player1.append(top2)
    else:
        player2.append(top2)
        player2.append(top1)
score = 0
rankingScore = None
if len(player1) > 0:
    rankingScore = player1
else:
    rankingScore = player2
mult = 1
rankingScore = list(reversed(rankingScore))
while len(rankingScore) > 0:
    top = rankingScore[0]
    rankingScore = rankingScore[1:]
    score += mult*top
    mult += 1
print(score)
