def pair(x,y):
    return (x*x + x + 2*x*y + 3*y + y*y )/2

x1 = 42421237
x2 = 2820297

c2 = 2+4*pair(x1, x2)

c1 = 4+4*pair(16, c2)

c = 2+4*pair(241, c1)

print(c)