
'''
sum = 0
countUp = 0
countDown = 0
maxCountUp = 0
maxCountDown = 0


f = open('10m.txt', 'r')
l = [int(line) for line in f]
lens = len(l)+1
maxi = l[0]
mini = l[0]

if lens %2 == 0:
    a = lens//2
    median = (l[a]+l[a+1])/2
else: median = l[lens//2]
for line in range(len(l)):
    sum += int(line)
    if l[line] > maxi:
        maxi = l[line]
    if l[line] < mini:
        mini = l[line]



print(maxi)
print(mini)


for i in range(len(l)-1):
    if l[i+1] > l[i]:
        countUp += 1
    else: countUp = 0
    if l[i+1] < l[i]:
        countDown += 1
    else: countDown = 0
    if countUp >= maxCountUp:
        maxCountUp = countUp
    if countDown >= maxCountDown:
        maxCountDown = countDown


sum = sum/(len(l)+1)


print(median)
print(sum)
print(maxCountUp)
print(maxCountDown)


f.close()


'''




























sum = 0
countUp = 0
countDown = 0
maxCountUp = 0
maxCountDown = 0


f = open('10m.txt', 'r')
l = [int(line) for line in f]
lens = len(l)+1

if lens %2 == 0:
    a = lens//2
    median = (l[a]+l[a+1])/2
else: median = l[lens//2]
for line in l:
    sum += int(line)

for i in range(len(l)-1):
    if l[i+1] > l[i]:
        countUp += 1
    else: countUp = 0
    if l[i+1] < l[i]:
        countDown += 1
    else: countDown = 0
    if countUp >= maxCountUp:
        maxCountUp = countUp
    if countDown >= maxCountDown:
        maxCountDown = countDown


sum = sum/(len(l)+1)

print(max(l))
print(min(l))
print(median)
print(sum)
print(maxCountUp)
print(maxCountDown)


f.close()
