from State import *
from Animal import *

g = Animal('goat')
c = Animal('cabbage')
w = Animal('wolf')

g.ident(w,c)
w.ident(None,g)
c.ident(g,None)

left = [w,g,c,'b']
right = []

start = State(left,right)
s = start.trav(c)
print(start)
print(s)

s.checkDanger()


