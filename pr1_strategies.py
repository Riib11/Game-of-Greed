def avgStrategy(myscore, theirscore, last):
    left = 100 - myscore
    dice = left // 3 # bases rolls on average roll
    return dice

def maxStrategy(myscore, theirscore, last):
    left = 100 - myscore
    dice = left // 5 # bases rolls on max roll
    return dice

def myStrategyVary(a,b):
    def strat(myscore, theirscore, last):
        left = 100 - myscore

        avg = 3
        std = 1.7

        dice = left//(avg + a*std)
        dice += b * (theirscore - myscore)

        if dice < 0:
            dice = 0
    
        return dice
    return strat