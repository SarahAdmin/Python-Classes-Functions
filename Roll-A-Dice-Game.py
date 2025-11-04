import random 
def DiceGame():
    dice = random.randrange(1,7)
    if (dice == 1): 
        print('You rolled number ',dice)
    elif (dice == 2): 
        print('A rolled number ',dice)
    elif (dice == 3): 
        print('A rolled number ',dice)
    elif (dice == 4): 
        print('A rolled number ',dice)
    elif (dice == 5): 
        print('A rolled number ',dice)
    elif (dice == 6): 
        print('A rolled number ',dice)
    else: 
        print('No number')
    return dice

if __name__ == "__main__": 
    rollAdice = DiceGame()
    print(rollAdice)
