class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def ident(self,pred,prey):
        self.pred = pred
        self.prey = prey
