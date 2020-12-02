x = [int(y) for y in open('Day1/input.txt').readlines()]
for i in range(0,len(x)):
    for j in range(1,len(x)):
        for k in range(2,len(x)):
            if x[i] + x[j] + x[k] == 2020:
                print(x[i]*x[j]*x[k]) #I'm sure there's some kind of pruning approach, but it's not cognitively faster than brute force

                #oh that's right; those starting points in the ranges should be pruned. WHoops!