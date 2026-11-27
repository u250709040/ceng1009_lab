
# def fizz_buzz(n):
#
#     for n in range(1, n + 1):
#         if n % 3 == 0 and n % 5 == 0:
#             print('FizzBuzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         elif n % 5 == 0:
#             print('Buzz')
#         else:
#             print(str(n))
#
#
# fizz_buzz(100)



# def digit_sum(n):
#     total = 0
#     while n > 0:
#         print(n)
#         total = total + n % 10
#         n = n // 10
#     return total
#
# print(digit_sum(1234))

# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s[i].upper()
#         else:
#             result = result + s[i].lower()
#
#     return result
#
# print(alternate_case("Hello World"))

# import turtle
#
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(3)
# t.speed(0)
# t.shape("circle")
# colors = ["red", "yellow" ,"blue"]
#
#
# def draw_polygon(t, sides, lenght):
#     for i in range(sides):
#         angle = 360 / sides
#         t.fd(lenght)
#         t.stamp()
#         t.lt(

# for i in range(3):
#     t.penup()
#     t.goto(-150 + i * 120, -30)
#     t.pendown()
#     t.color(colors[i])
#
#     draw_polygon(t, i + 3, 60)

# import turtle
#
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(3)
# t.speed(0)


# def filled_square(t, size , color):
#     t.fillcolor((color))
#     t.begin_fill()
#     for i in range (4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# for i in range(5):
#     t.penup()
#     t.goto(-165 + i * 70,-25)
#     t.pendown()
#     if i % 2 == 0:
#         filled_square(t,50, "red")
#     else:
#         filled_square(t,50, "blue")


# def draw_square(t, size,color):
#     t.penup()
#     t.goto(-size / 2, size / 2)
#     t.pendown()
#     for i in range(4):
#         t.fd(size)
#         t.right(90)
#
# for i in range(12):
#     t.left(30)
#     draw_square(t, 80, "red")


# def draw_square(t, size , filled):
#     if filled:
#         t.begin_fill()
#     for i in range (4):
#         t.forward(size)
#         t.left(90)
#     if filled:
#         t.end_fill()
#
# size = 40
#
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120 + col * size , -120 + row * size)
#         t.pendown()
#         draw_square(t, size, (row + col) % 2 == 0)
#
#
#
# wn.exitonclick()


