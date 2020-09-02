#Counter
from collections import Counter
a= "aaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.items())
print(my_counter.keys())
print(my_counter.most_common(1))

#tuple
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)

#Ordered Dictionary
from collections import OrderedDict
ordered_dict =  OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 3
ordered_dict['c'] = 2
print(ordered_dict)

#default Dictionary
from collections import defaultdict
d = defaultdict( list )
d['a'] = 1.56
d['b'] = 2
print(d['a'])#error?

#deque
from collections import deque
d = deque()
d.append("a")
d.append(1)

d.appendleft(5)
print(list(d))

d.popleft()
print(list(d))

d.extend([4,5,6])
print(list(d))

d.extendleft([4,5,6])
print(list(d))

d.rotate(1)
print(list(d))