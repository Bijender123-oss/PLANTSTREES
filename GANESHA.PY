import turtle
import time

# Screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Lalbaugcha Raja 🙏")

screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)
t.color("#FFD700")

# -------------------------
# LINE DRAW FUNCTION
# -------------------------

def line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


def circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    t.circle(radius)


def arc(x, y, radius, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.circle(radius, angle)


# -------------------------
# GANESH JI KA CROWN
# -------------------------

# Crown outline
line(-100, 190, -70, 270)
line(-70, 270, 0, 320)
line(0, 320, 70, 270)
line(70, 270, 100, 190)

# Crown decoration
line(-70, 270, 0, 250)
line(0, 250, 70, 270)

circle(0, 285, 12)

# Crown lines
for x in range(-60, 61, 20):
    line(x, 270, x, 300)

# -------------------------
# EARS
# -------------------------

# Left ear
arc(-100, 100, 80, 180)

# Right ear
arc(100, 100, 80, -180)

# Ear inner lines
arc(-100, 110, 55, 160)
arc(100, 110, 55, -160)

# -------------------------
# HEAD
# -------------------------

# Head outline
arc(0, 90, 120, 180)
arc(0, 90, 120, -180)

# -------------------------
# EYES
# -------------------------

# Left eye
arc(-45, 145, 22, 180)
arc(-45, 145, 22, -180)

# Right eye
arc(45, 145, 22, 180)
arc(45, 145, 22, -180)

# Eye pupils
circle(-45, 140, 5)
circle(45, 140, 5)

# -------------------------
# TILAK
# -------------------------

line(-10, 200, 0, 220)
line(0, 220, 10, 200)

line(-5, 200, 0, 190)
line(0, 190, 5, 200)

# -------------------------
# TRUNK
# -------------------------

# Left curve
t.penup()
t.goto(-25, 120)
t.setheading(-70)
t.pendown()
t.circle(100, 90)

# Right curve
t.penup()
t.goto(25, 120)
t.setheading(-110)
t.pendown()
t.circle(-100, 90)

# Trunk tip
arc(0, 10, 40, 180)

# -------------------------
# BODY
# -------------------------

# Body outline
arc(0, -100, 170, 180)
arc(0, -100, 170, -180)

# Belly decoration
arc(0, -160, 100, 180)
arc(0, -160, 100, -180)

# -------------------------
# ARMS
# -------------------------

# Left arm
line(-110, -20, -200, -100)
line(-200, -100, -180, -150)

# Right arm
line(110, -20, 200, -100)
line(200, -100, 180, -150)

# Blessing hand
circle(-180, -70, 25)

# -------------------------
# JEWELLERY
# -------------------------

# Necklace
arc(0, 20, 80, 180)
arc(0, 20, 80, -180)

# Necklace beads
for x in range(-50, 51, 25):
    circle(x, 0, 5)

# -------------------------
# MODAK
# -------------------------

line(100, -200, 150, -200)
line(150, -200, 125, -150)
line(125, -150, 100, -200)

# -------------------------
# FINAL MESSAGE
# -------------------------

screen.update()

t.penup()
t.goto(0, -350)
t.color("#FFD700")
t.write(
    "GANPATI BAPPA MORIYA 🙏",
    align="center",
    font=("Arial", 22, "bold")
)

screen.update()

turtle.done()