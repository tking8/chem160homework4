from point import *
p1=point(3, [1., 2., 3.])
p1
p2=point(3, [6., 7., 8.])
print("p1 dist p2=", p1.dist(p2))
p2.mirror()
print(p2)
