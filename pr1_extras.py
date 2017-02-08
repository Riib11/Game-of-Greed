from pr1 import *
from pr1_strategies import *

class ab_result:
    def __init__(self,a,b,wr,o_wr,tr):
        self.a = a
        self.b = b
        self.wr = wr
        self.o_wr = o_wr
        self.tr = tr
    def printSelf(self):
        print("wr: " + str(100*self.wr) + "%")
        print("other wr: " + str(100*self.o_wr) + "%")
        print("tr: " + str(100*self.tr) + "%")
        print("a: " + str(self.a))
        print("b: " + str(self.b))

def test_range(min_a,max_a,it_a,min_b,max_b,it_b,tests,strat2):
    iterations_a = int((max_a - min_a) // it_a)
    iterations_b = int((max_b - min_b) // it_b)

    max_ab_result = ab_result(min_a,min_b,0,0,0)

    i = 0
    for ti in tqdm(range(0,iterations_a+1)):
        a = min_a + (it_a*i)
        for j in range(0,iterations_b+1):
            b = min_b + (it_b*j)
            r = test_trial(a,b,strat2,tests)
            if r.wr > max_ab_result.wr:
                max_ab_result = r
        i += 1
    max_ab_result.printSelf()


def test_trial(a,b,strat2,tests):
    r = manyGamesQuiet(myStrategyVary(a,b),strat2,tests)
    return ab_result(a,b,r[0],r[1],r[2])

def manyGamesQuiet(strat1, strat2, n):
    wins1 = 0
    wins2 = 0
    ties = 0

    for i in range(0,n):
        result = autoplay(strat1,strat2)
        if result == 1:
            wins1 += 1
        elif result == 2:
            wins2 += 1
        elif result == 3:
            ties += 1

    return [wins1/n, wins2/n, ties/n]

def compareStrategies(stratsArray,n):
    scores = {}
    for strat in stratsArray:
        scores[strat] = 0
    scores['ties'] = 0

    games = 0

    for strat1 in stratsArray:
        for strat2 in stratsArray:
            if strat1 != strat2:
                games += 1
                result = manyGamesQuiet(strat1,strat2, n)
                if result == 1:
                    scores[strat1] += 1
                elif result == 2:
                    scores[strat2] += 1
                elif result == 3:
                    scores['ties'] += 1

    for k, v in scores.items():
        print(str(k) + ": " + str(100*v/games) + "% (" + str(v) + ")")

def testForTheirEffect(strat):
    deviants_list = []
    for myscore in range(0,100):
        default_roll = strat(myscore, 0, False) # to start off
        deviants = {}
        for theirscore in range(0,101):
            r = strat(myscore,theirscore, False)
            if r != default_roll:
                deviants[[myscore,theirscore]] = r - default_roll
        deviants_list.append(deviants)

    x = 0
    print("Start")
    for deviants in deviants_list:
        if len(deviants) != 0:
            print()
            print("Deviants for myscore=" + str(x))
            for k,v in deviants.items():
                print("myscore=" + str(k[0]) + ", theirscore=" + str(k[1]) + ", dev=" + str(v))
            x += 1
    print("End")