import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
colormode(255)


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(15):
#     timmy.forward(15)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# directions = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

# def draw_shape(n):
#     timmy.color(random.choice(colors))
#     for j in range(n):
#         timmy.forward(100)
#         timmy.right(360 / n)
#
#
# for i in range(3, 11):
#     draw_shape(i)

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
