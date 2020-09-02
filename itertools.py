from itertools import product 
a = [1, 2]
b = [3]
prod = product(a,b, repeat =2)
print(list(prod))

#Permutations
from itertools import permutations 
a = [1, 2, 3]
per = permutations(a)
print(list(per))

#Combinations
from itertools import combinations#,combinations_with_replacements  
a = [1, 2, 3]
comb = combinations(a, 2)
print(list(comb))

#accumulate
from itertools import accumulate
import operator 
a = [1, 2, 3, 5]
acc = accumulate(a, func = operator.mul)
print(list(acc))


#groupby
def smaller_than_3(x):
    return x < 3
from itertools import groupby  
a = [1, 2, 3, 4]
g = groupby(a, key = smaller_than_3 )
print(g)

#infinite iterations



