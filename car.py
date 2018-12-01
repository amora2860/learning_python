from graphics import *
from wheel import *




new_win = GraphWin("A Car", 700, 300)

rect = Rectangle(Point(30,10), Point(220,100))
rect.setFill("blue")
rect.draw(new_win)
# What we'll need for the wheel...
wheel_center = Point(200, 100)  # The wheel center is a Point at (200, 200)
wheel_center2 = Point(50,100)
tire_radius = 50 # The radius of the outer tire is 100
# Make a wheel object
new_wheel1 = Wheel(wheel_center, 0.6 * tire_radius, tire_radius)
new_wheel2 = Wheel(wheel_center2, 0.6 * tire_radius, tire_radius)
# Set its color
new_wheel1.set_color('red', 'black')
new_wheel2.set_color('red', 'black')
# And finally, draw it
new_wheel1.draw(new_win)
new_wheel2.draw(new_win)

new_win.mainloop()
