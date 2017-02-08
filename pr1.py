import random
import math
import pr1testing
from tqdm import tqdm
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1,strat2):
    player1 = str(strat1)
    player2 = str(strat2)
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = strat1(score1,score2,last)
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = strat2(score2,score1,last)
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplay(strat1, strat2):
    player1 = str(strat1)
    player2 = str(strat2)
    score1 = 0
    score2 = 0
    last = False
    while True:
        numDice = strat1(score1,score2,last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        numDice = strat2(score2,score1,last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n):
    wins1 = 0
    wins2 = 0
    ties = 0

    for ti in tqdm(range(0,n)):
        result = autoplay(strat1,strat2)
        if result == 1:
            wins1 += 1
        elif result == 2:
            wins2 += 1
        elif result == 3:
            ties += 1

    print(str(strat1) + ": " + str(100*wins1/n) + "% (" + str(wins1) + ")")
    print(str(strat2) + ": " + str(100*wins2/n) + "% (" + str(wins2) + ")")
    print("ties: " + str(100*ties/n) + "% (" + str(ties) + ")")

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif myscore >= 51 and myscore <=80:
        return 10
    elif myscore > 80:
        return 0

def improve(strat1):
    def improvedStrategy(myscore, theirscore, last):
        if myscore == 100:
            return 0
        else:
            return strat1(myscore,theirscore,last)
    return improvedStrategy

def myStrategy(myscore, theirscore, last):
    a = 0.0134
    left = 100 - myscore

    avg = 3
    std = 1.7

    dice = int(left // (avg + a*std))
    if dice < 0:
        dice = 0
    return dice