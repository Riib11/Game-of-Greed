from pr1 import *
from pr1_strategies import *

class trial_result:
    def __init__(self,a,b,c,wr,o_wr,tr):
        self.a = a
        self.b = b
        self.c = c
        self.wr = wr
        self.o_wr = o_wr
        self.tr = tr
    def printSelf(self):
        print("wr: " + str(100*self.wr) + "%")
        print("other wr: " + str(100*self.o_wr) + "%")
        print("tr: " + str(100*self.tr) + "%")
        print("a: " + str(self.a))
        print("b: " + str(self.b))
        if(self.c != -1):
            print("c: " + str(self.c))

def test_rangeABC(min_a,max_a,it_a,min_b,max_b,it_b,min_c,max_c,it_c,tests,strat2):
    iterations_a = int((max_a - min_a) // it_a)
    iterations_b = int((max_b - min_b) // it_b)
    iterations_c = int((max_c - min_c) // it_c)

    max_trial_result = trial_result(min_a,min_b,min_c,0,0,0)

    # cycling through a,b,c
    i = 0
    for ti in tqdm(range(0,iterations_a+1)):
        a = min_a + (it_a*i)
        for j in range(0,iterations_b+1):
            b = min_b + (it_b*j)
            for k in range(0,iterations_c+1):
                c = min_c + (it_c*k)
                
                r = test_trial(a,b,c,strat2,tests)
                if r.wr > max_trial_result.wr:
                    max_trial_result = r
    i += 1

def test_rangeAB(min_a,max_a,it_a,min_b,max_b,it_b,tests,strat2,reverse):
    iterations_a = int((max_a - min_a) // it_a)
    iterations_b = int((max_b - min_b) // it_b)

    max_trial_result = trial_result(min_a,min_b,-1,0,0,0)

    # cycling through a,b
    i = 0
    for ti in tqdm(range(0,iterations_a+1)):
        a = min_a + (it_a*i)
        for j in range(0,iterations_b+1):
            b = min_b + (it_b*j)

            c = -1

            r = test_trial(a,b,c,strat2,tests,reverse)
            
            if r.wr > max_trial_result.wr:
                max_trial_result = r
                print(r.a,r.b,r.wr)
        i += 1

    max_trial_result.printSelf()


def test_trial(a,b,c,strat2,tests,reverse):
    if c == -1:
        strat1 = myStrategyVaryAB(a,b)
    else:
        strat1 = myStrategyVaryABC(a,b,c)

    if reverse:
        strat1, strat2, = strat2, strat1

    r = manyGamesQuiet(strat1,strat2,tests)

    return trial_result(a,b,c,r[0],r[1],r[2])

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