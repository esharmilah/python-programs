import random as ra
p=''
a=[chr(x) for x in range(ord('a'),ord('z')+1)]
d=[int(x) for x in range(10)]
for r in range(4):
    p+=ra.choice(a)
    p+=str(ra.choice(d))
    print(p)
