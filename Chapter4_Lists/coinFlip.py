import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlipList  = []
    for i in range(100):
        coinFlipList.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    coinFlipListStr = ''
    for i in range(len(coinFlipList)):
        coinFlipListStr =coinFlipListStr + str(coinFlipList[i])
    
    if ('000000' in coinFlipListStr) or ('111111' in coinFlipListStr):
        numberOfStreaks += 1

print(numberOfStreaks)        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))