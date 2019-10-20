class State:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.routes = {}
    
    def __str__(self):
        return "Left: "+str(self.left)+" and Right: "+str(self.right)
    def __repr__(self):
        return "Left: "+str(self.left)+" and Right: "+str(self.right)
    def checkDanger(self):
        for a in self.left:
            if a.pred in self.left: 
                return True
        for a in self.right:
            if a.pred in self.right:
                return True
        return False

    def trav(self,pas):
        #   TODO handle empty trav
        s = State(self.left[:],self.right[:])
        sr,de = s.left,s.right if 'b' in s.left else s.rights.left
        sr.remove(pas)
        sr.remove('b')
        de.extend([pas,'b'])
        self.routes[pas] = s
        return s

    def getRoutes(self):
        for pas,s in self.items():
            print("Take"+pas+"across to: "+s)

