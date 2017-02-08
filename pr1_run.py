from pr1 import *
from pr1_extras import *
from pr1_strategies import *
from max_finder import *

"""
# doesn't win against:
- test9
- test10
- test11
"""

"""
Notes:
- which strategy goes first matters
- write tester to iterate over a and find the a with max wr against test9-11
"""

# manyGames(pr1testing.test9, pr1testing.test10, 10000)

# compareStrategies([pr1testing.test1, pr1testing.test2, pr1testing.test3, pr1testing.test4, pr1testing.test5, pr1testing.test6, pr1testing.test7, pr1testing.test8, pr1testing.test9, pr1testing.test10, pr1testing.test11], 10000)

# manyGames(sample2, myStrategy, n):

# min_a = -1
# max_a = 1
# it_a = .001

# min_b = -1
# max_b = 1
# it_b = .01

min_a = 0.134
max_a = 0.134
it_a = 0.001

min_b = -0.001
max_b = 0.001
it_b = 0.0001

min_c = -1
max_c = 1
it_c = 0.1

tests = 10000
strat2 = pr1testing.test9

# test_rangeAB(min_a,max_a,it_a,min_b,max_b,it_b,tests,strat2,False)

# max_finderAB(a,b,step_a,step_b,tests,reverse,strat2)
max_finderABC(1,1,1,.1,.1,.1,tests,False,strat2).printSelf()


# pr1testing.testStrat(myStrategy, 10000)