# import turtle

# -- setup --

# wn = turtle.Screen()
# wn.bgcolor("Lightgreen")
# tess = turtle.Turtle()
# tess.speed(1000)

# -- functions --

# def  drawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesides
#     for i in range(somesides):
#         someturtle.fd(somesize)
#         someturtle.left(angle)
#
# def drawSpiral(someturtle, angle):
#     size = 1
#     for i in range(200):
#         someturtle.fd(size)
#         someturtle.right(angle)
#         size = size + 1
#
# def drawEquitriangle(someturtle, somesize):
#     drawPoly(someturtle, 3 , somesize)
#
# def drawStar(someturtle, size):
#     for i in range(5):
#         someturtle.fd(size)
#         someturtle.right(144)
#
# def drawSprite(someturtle, legs , length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.fd(length)
#         someturtle.backward(length)
#         someturtle.left(angle)

# -- exercises --

# Exercise 1

# tess.color("hotpink")
# drawPoly(tess, 8, 50)

# Exercise 2

# tess.color("blue")
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)


# Exercise 3
#

# tess.color("blue")
# tess.penup()
# tess.goto(-150, 0)
# tess.pendown()
#
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150, 0)
# tess.pendown()
#
# drawSpiral(tess, 89)


# Exercise 4

# drawEquitriangle(tess, 100)

# Exercise 5

# tess.color("hotpink")
#
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawStar(tess, 100)
#
# for i in range(5):
#     drawStar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

# # Exercise 6
#
# tess.color("red")
# tess.pensize(5)
# drawSprite(tess, 15, 120)
#
#
#
#
#
# # -- finish --
# wn.exitonclick()




