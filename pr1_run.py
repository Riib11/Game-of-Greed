from pr1 import *
from pr1_extras import *
from pr1_strategies import *

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

min_a = -1
max_a = 1
it_a = .01

min_b = -1
max_b = 1
it_b = .01

tests = 1000
strat2 = pr1testing.test9

test_range(min_a,max_a,it_a,min_b,max_b,it_b,tests,strat2)