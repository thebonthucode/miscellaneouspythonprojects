import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=500, height=500)
screen.tracer(0)

player = turtle.Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.speed(0)
player.goto(0, -200)
player.direction = "stop"

enemies = []

for _ in range(10):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    enemy.goto(x, y)
    enemy.dx = random.randint(-5, 5)
    enemy.dy = random.randint(-5, 5)
    enemies.append(enemy)

def move_left():
    x = player.xcor()
    x -= 3
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 3
    player.setx(x)

def stop():
    player.direction = "stop"

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(stop, "space")

def update_screen():
    screen.update()
    screen.ontimer(update_screen, 5)

while True:
    for enemy in enemies:
        x = enemy.xcor()
        y = enemy.ycor()
        x += enemy.dx
        y += enemy.dy
        enemy.setx(x)
        enemy.sety(y)

        if enemy.distance(player) < 20:
            player.color("red")
            player.shape("triangle")
            player.goto(0, 0)
            player.direction = "stop"
            for enemy in enemies:
                enemy.hideturtle()
            break
        if enemy.xcor() < -290 or enemy.xcor() > 290:
            enemy.dx *= -1
        if enemy.ycor() < -290 or enemy.ycor() > 290:
            enemy.dy *= -1
    update_screen()
