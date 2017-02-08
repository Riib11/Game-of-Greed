from pr1 import *
from pr1_strategies import *
from pr1_extras import *

# find max wr on plane AB
def max_finderAB(a,b,step_a,step_b,tests,reverse,strat2):
    end = False
    
    curr = test_trial(a,b,-1,strat2,tests,reverse)
    last = None

    while not end:
        # check the 8 positions around (a,b)
        for da in [-step_a,0,step_a]:
            x = a + da
            for db in [-step_b,0,step_b]:
                y = b + db
                r = test_trial(x,y,-1,strat2,tests,reverse)
                if r.wr > curr.wr:
                    curr = r
        # curr is now at the r that with highest wr

        # if curr hasn't changed, then the max has been found
        if last != None and last.wr == curr.wr:
            end = True

        # save this round as last
        last = curr

        # set a,b to now be the position of the new curr
        a = curr.a
        b = curr.b
        print("#",end="")
    print()
    return curr

# find max wr on space ABC
def max_finderABC(a,b,c,step_a,step_b,step_c,tests,reverse,strat2):
    end = False
    
    curr = test_trial(a,b,c,strat2,tests,reverse)
    last = None

    while not end:
        # check the positions around (a,b,c)
        for da in [-step_a,0,step_a]:
            x = a + da
            for db in [-step_b,0,step_b]:
                y = b + db
                for dc in [-step_c,0,step_c]:
                    z = c + dc
                    r = test_trial(x,y,c,strat2,tests,reverse)
                    if r.wr > curr.wr:
                        curr = r
        # curr is now at the r that with highest wr

        # if curr hasn't changed, then the max has been found
        if last != None and last.wr == curr.wr:
            end = True

        # save this round as last
        last = curr

        # set a,b to now be the position of the new curr
        a = curr.a
        b = curr.b
        c = curr.c
        print("#",end="")
    print()
    return curr

def z(x,y):
    return -((x+1)**2)-((y+2)**2)

def max_finder(a,b,step_a,step_b):
    end = False
    
    curr_x, curr_y = a,b
    curr = z(a,b)
    last = -10000

    while not end:
        # check the 8 positions around (a,b)
        for da in [-step_a,0,step_a]:
            x = a + da
            for db in [-step_b,0,step_b]:
                y = b + db
                r = z(x,y)
                if r > curr:
                    curr_x,curr_y = x,y
                    curr = r
        # curr is now at the r that with highest z

        # if curr hasn't changed, then the max has been found
        if last == curr:
            end = True

        # save this round as last
        last = curr

        # set a,b to now be the position of the new curr
        a = curr_x
        b = curr_y

max_finder(10,10,1,1)