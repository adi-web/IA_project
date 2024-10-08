class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.g=None

        # variabili solo per A*
        self.h=None
        self.f=None


    def __str__(self):
        return f"Node with x={self.x} and y={self.y}"

    def __repr__(self):
        return f"Node with x={self.x} and y={self.y}"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,new_x):
        self.x=new_x

    def setY(self, new_y):
        self.y = new_y

    def setG(self,new_g):
        self.g=new_g

    def setH(self, new_h):
        self.h = new_h

    def setF(self, new_f):
        self.f = new_f

    def getH(self):
        return self.h
    def getG(self):
        return self.g
    def getF(self):
        return self.f

    def getVertex(self):
        return (self.x,self.y)
