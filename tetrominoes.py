from graphics import *


#shape should take whatever the center points are and convert them into points
# for the rectangle class to be able o draw.
class Shape(Rectangle):
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, color3):

        Rectangle.__init__(self, p1, p2)
        self.color3 = color3
        self.box1 = Rectangle(p2, p3)
        self.box2 = Rectangle(p4, p5)
        self.box3 = Rectangle(p6, p7)
        self.box4 = Rectangle(p8, p9)
        self.box1.setFill(color3)
        self.box2.setFill(color3)
        self.box3.setFill(color3)
        self.box4.setFill(color3)
    def draw(self, win):

        self.box1.draw(win)
        self.box2.draw(win)
        self.box3.draw(win)
        self.box4.draw(win)


class I_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 30, p1.y + 10)
        p7 = Point(p1.x + 60, p1.y - 20)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 60, p1.y + 10)
        p9 = Point(p1.x + 90, p1.y - 20)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class J_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 30, p1.y + 10)
        p7 = Point(p1.x + 60, p1.y - 20)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 30, p1.y + 10) # left lower point
        p9 = Point(p1.x + 60, p1.y + 40) # right upper point


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class L_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x -30, p1.y + 10)
        p5 = Point(p1.x + 0, p1.y + 40)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 0, p1.y + 10)
        p7 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 30, p1.y + 10)
        p9 = Point(p1.x + 60, p1.y - 20)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class O_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + -30, p1.y -20)  #left lower point
        p7 = Point(p1.x + 0, p1.y - 50)  # right upper point
        #    This block goes to the right of block three
        p8 = Point(p1.x + 0, p1.y - 20)
        p9 = Point(p1.x + 30, p1.y - 50)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class S_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 0, p1.y - 20)
        p7 = Point(p1.x + 30, p1.y - 50)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 30, p1.y - 20)
        p9 = Point(p1.x + 60, p1.y - 50)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class T_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 30, p1.y + 10)
        p7 = Point(p1.x + 60, p1.y - 20)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 0, p1.y + 10)
        p9 = Point(p1.x + 30, p1.y + 40)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

class Z_shape(Shape):
    def __init__(self, p1):
        self.p1 = p1
        #This is Block one.
        p2 = Point(p1.x -30, p1.y + 10)
        p3 = Point(p1.x + 0, p1.y - 20)
    #    This block goes to the right of block one
        p4 = Point(p1.x + 0, p1.y + 10)
        p5 = Point(p1.x + 30, p1.y - 20)
        #    This block goes to the right of block two
        p6 = Point(p1.x + 0, p1.y + 10)
        p7 = Point(p1.x + 30, p1.y + 40)
        #    This block goes to the right of block three
        p8 = Point(p1.x + 30, p1.y + 10)
        p9 = Point(p1.x + 60, p1.y + 40)


        Shape.__init__(self, p1,p2, p3, p4,p5,p6,p7,p8,p9, "blue")

win = GraphWin("Tetrominoes", 900, 200)


tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
x = 40

for i in tetrominoes:
    shape = i(Point(x,150))
    shape.draw(win)
    x = x +125


win.mainloop()
