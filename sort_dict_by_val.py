xs={'a':2,'b':5,'c':0,'d':1}

print(xs.items())
sort_vals=sorted(xs.items(),key=lambda x:x[1])

print(sort_vals)

import operator
import functools

sort_val1=sorted(xs.items(),key=operator.itemgetter(1))

print(sort_val1)

nos_add=[45,60,25]

added_vals=functools.reduce(lambda x,y:x+y,nos_add)
print(added_vals)