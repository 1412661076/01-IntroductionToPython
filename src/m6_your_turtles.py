"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Rui Fang.
"""
###############################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(5)

T1 = rg.SimpleTurtle('blank')
T1.pen = rg.Pen('LightSkyBlue', 2)
T1.speed = 10


T1.pen_up()
T1.go_to(rg.Point(0,100))
T1.pen_down()
T1.draw_circle(40)
T1.pen_up()
T1.go_to(rg.Point(-18, 150))
T1.pen_down()
T1.draw_circle(5)
T1.pen_up()
T1.go_to(rg.Point(18,150))
T1.pen_down()
T1.draw_circle(5)
T1.pen_up()
T1.go_to(rg.Point(-15,120))
T1.pen_down()
T1.go_to(rg.Point(15,120))
T1.pen_up()
T1.go_to(rg.Point(0,100))
T1.pen_down()
T1.go_to(rg.Point(0,-50))
T1.go_to(rg.Point(0,56))
T1.left(45)
T1.forward(100)
T1.backward(100)
T1.left(90)
T1.forward(100)
T1.backward(100)



T2 = rg.SimpleTurtle('blank')
T2.pen = rg.Pen('red', 2)
T2.speed = 1
T2.go_to(rg.Point(x,y))
window.close_on_mouse_click()
