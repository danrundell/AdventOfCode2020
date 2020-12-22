text = open('Day22/input.txt').read().split('\n\n')

p1 = [int(x) for x in text[0].strip().split('\n')[1:]]
p2 = [int(x) for x in text[1].strip().split('\n')[1:]]

def playGame(player1, player2):
    rounds = set()
    while len(player1) > 0 and len(player2) > 0:
        roundKey = ','.join([str(x) for x in player1]) + '|' + ','.join([str(x) for x in player2])
        if roundKey in rounds:
            return (1, player1)
            break
        else:
            rounds.add(roundKey)
        top1 = player1[0]
        top2 = player2[0]
        player1 = player1[1:]
        player2 = player2[1:]
        if len(player1) >= top1 and len(player2) >= top2:
            recursiveresult = playGame(player1[0:top1],player2[0:top2])
            if recursiveresult[0] == 1:
                player1.append(top1)
                player1.append(top2)
            else:
                player2.append(top2)
                player2.append(top1)
        elif top1 > top2:
            player1.append(top1)
            player1.append(top2)
        else:
            player2.append(top2)
            player2.append(top1)
    if len(player1) > 0:
        return (1, player1)
    else:
        return (2, player2)

f = playGame(p1,p2)
rankingScore = f[1]

score = 0
mult = 1
rankingScore = list(reversed(rankingScore))
while len(rankingScore) > 0:
    top = rankingScore[0]
    rankingScore = rankingScore[1:]
    score += mult*top
    mult += 1
print(score)
