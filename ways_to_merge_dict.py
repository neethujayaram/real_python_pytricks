x={1:'a',2:'b'}
y={2:'c',3:'d'}

z={**x,**y}

print(z)



x={'a':1,'b':2}
y={'b':3,'d':4}

z=dict(x, **y)
print(z)