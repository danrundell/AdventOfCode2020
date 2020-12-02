x = [int(y) for y in open('Day1/input.txt').readlines()]
for i in range(0,len(x)):
    for j in range(1,len(x)):
        if x[i] + x[j] == 2020:
            print(x[i]*x[j])