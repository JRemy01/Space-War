import os
import random
import time
import turtle



turtle.fd(0)
# speed of animation. 0 the max
turtle.speed(0)
# backgrounf colo
turtle.bgcolor("Black")
# titre
turtle.title("Space War")
# background image
turtle.bgpic("anti.gif")
# Hide the default arrow
turtle.ht()
# save memory
turtle.setundobuffer(1)

# speed up drawing
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape =spriteshape)
        self.speed(0)
        # No pen
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto( startx, starty)
        self.speed = 1

    def Move(self):
        self.fd(self.speed)

        # boundary detection
        if self.xcor()> 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def Arreter(self):
        self.speed =0

    def is_collision(self,other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Players(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 1
        self.lives = 3
        
 
    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Ennemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0,360))

    def Move(self):
        self.fd(self.speed)

        # boundary detection
        if self.xcor()> 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Explosion(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.1, stretch_len = 0.1, outline = None )
        self.goto(-1000,1000)
        self.frame = 0

    def explode(self,startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1 

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000,1000)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.score_pl_2 = 0
        self.lives = 3
        self.lives_pl_2 = 3

        self.border_pen = turtle.Turtle()
        self.text_pen = turtle.Turtle()

        for pen in (self.border_pen, self.text_pen):
            pen.speed(0)
            pen.penup()
            pen.hideturtle()
            pen.color("white")

    def border(self):
        self.border_pen.pensize(3)
        self.border_pen.goto(-300, 300)
        self.border_pen.pendown()
        for side in range(4):
            self.border_pen.fd(600)
            self.border_pen.rt(90)
        self.border_pen.penup()

    def affiche_statut(self):
        self.text_pen.clear() 
        self.text_pen.goto(-300, 310)
        self.text_pen.write(f"Score: {self.score}", font=("Arial", 16, "normal"))
        self.text_pen.goto(-300, 280)
        self.text_pen.write(f"Lives: {self.lives}", font=("Arial", 16, "normal"))

        # Player 2
        self.text_pen.goto(245, 310)
        self.text_pen.write(f"Score: {self.score_pl_2}", font=("Arial", 16, "normal"))
        self.text_pen.goto(245, 280)
        self.text_pen.write(f"Lives: {self.lives_pl_2}", font=("Arial", 16, "normal"))

        # vie
        if self.lives == 0:
            self.text_pen.goto(-50, 0)
            self.text_pen.write(f"Game Over !", font=("Arial", 55, "normal"))
            self.text_pen.goto(-50, -100)
            self.text_pen.write(f"Player 2 Won !", font=("Arial", 35, "normal"))

        if self.lives_pl_2 == 0:
            self.text_pen.goto(-50, 0)
            self.text_pen.write(f"Game Over !", font=("Arial", 55, "normal"))
            self.text_pen.goto(-50, -100)
            self.text_pen.write(f"Player 1 Won !", font=("Arial", 35, "normal"))

        if (self.lives == 0) & (self.lives_pl_2 == 0):
            self.text_pen.goto(-50, 0)
            self.text_pen.write(f"Egalite !", font=("Arial", 55, "normal"))




class Arme_player_1(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None )
        self.speed = 20
        self.status = "ready"
        self.goto(-1000,1000)

    def tire(self):
        if self.status == "ready":
            # son
            os.system("afplay laser.mp3&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "tire"

    def move(self):

        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "tire":
            self.fd(self.speed)

        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class Arme_player_2(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None )
        self.speed = 20
        self.status = "ready"
        self.goto(-1000,1000)

    def tire(self):
        if self.status == "ready":
            # son
            os.system("afplay boomerang.mp3&")
            self.goto(player_2.xcor(), player_2.ycor())
            self.setheading(player_2.heading())
            self.status = "tire"

    def move(self):

        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "tire":
            self.fd(self.speed)

        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


game = Game()

# limite
game.border()
# affiche statut
game.affiche_statut()

# Create player 1
x_player_1 = random.randint(-280,280)
y_player_1 = -280
player = Players("turtle", "yellow",x_player_1,y_player_1)
player.setheading(90)

# Create player 2
x_player_2 = random.randint(-280,280)
y_player_2 = 280
player_2 = Players("turtle","green",x_player_2,y_player_2)
player_2.setheading(270)

# allies
#ally = Ally("square", "blue",0,0)
allies = []
for i in range(6):
    allies.append(Ally("square", "blue",random.randint(-280,280),-300))

# arme
arme_pl_1 = Arme_player_1("triangle","orange",0,0)
arme_pl_2 = Arme_player_2("triangle","orange",0,0)

# create ennemys 
#ennemy = Ennemy("circle", "red",200,100)
enemies = []
for i in range(6):
    enemies.append(Ennemy("circle", "red",random.randint(-280,280),300))


explosions = []
for i in range(20):
    explosions.append(Explosion("circle", "orange",0,0))
# keyboard bondings  Player 1
turtle.onkey(player.turn_left, "Left") # touch right : turn left
turtle.onkey(player.turn_right, " Right") # touch left : turn right
turtle.onkey(player.accelerate, "Up")  # touch Up : accelerate 
turtle.onkey(player.decelerate, "Down")  # touch Down : decelerate
turtle.onkey(arme_pl_1.tire, "space")  # touch space : tire

# keyboard bondings  Player 2
turtle.onkey(player_2.turn_right, "d") # touch right : turn left
turtle.onkey(player_2.turn_left, "q") # touch left : turn right
turtle.onkey(player_2.accelerate, "z")  # touch Up : accelerate 
turtle.onkey(player_2.decelerate, "s")  # touch Down : decelerate
turtle.onkey(arme_pl_2.tire, "k")  # touch space : tire


turtle.listen()

# Detection de collision
def detect_collision(sprite1, sprite2, threshold=20):
    distance = sprite1.distance(sprite2)
    return distance < threshold


while True:
    turtle.update()
    time.sleep(0.03)

    player.Move()
    player_2.Move()
    arme_pl_1.move()
    arme_pl_2.move()

    for ennemy in enemies:
        ennemy.Move()

        # if collision with ennemy
        if player.is_collision(ennemy):
            # son
            os.system("afplay explosion.mp3&")
            game.lives -= 1
            player.goto(random.randint(-280,280), -280)
            player.speed = 0
            game.score -= 100
            game.affiche_statut()
            for explose in explosions:
                explose.explode(ennemy.xcor(), ennemy.ycor())
            if game.lives <= 0:
                player.ht()
                game.state = "game_over"

        # player attack ennemy allies
        if arme_pl_1.is_collision(ennemy):
            # son
            os.system("afplay explosion.mp3&")
            x = random.randint(-280,280)
            y = 300
            ennemy.goto(x,y)
            arme_pl_1.status = "ready"
            game.score += 100
            game.affiche_statut()
            for explose in explosions:
                explose.explode(arme_pl_1.xcor(), arme_pl_1.ycor())

        # player 2 attack ennemy (ally) 
        if arme_pl_2.is_collision(ennemy):
            # son
            os.system("afplay explosion.mp3&")
            x = random.randint(-280,280)
            y = 300
            ennemy.goto(x,y)
            arme_pl_2.status = "ready"
            game.score_pl_2 -= 50
            game.affiche_statut()
            for explose in explosions:
                explose.explode(arme_pl_2.xcor(), arme_pl_2.ycor())
        


    for ally in allies:
        ally.Move()

        # player attack ally
        if arme_pl_1.is_collision(ally):
            # son
            os.system("afplay explosion.mp3&")
            x = random.randint(-280,280)
            y = -300
            ally.goto(x,y)
            arme_pl_1.status = "ready"
            game.score -= 50
            game.affiche_statut()
            for explose in explosions:
                explose.explode(arme_pl_1.xcor(), arme_pl_1.ycor())

        # player 2 attack ennemy (ally)
        if arme_pl_2.is_collision(ally):
            # son
            os.system("afplay explosion.mp3&")
            x = random.randint(-280,280)
            y = -300
            ally.goto(x,y)
            arme_pl_2.status = "ready"
            game.score_pl_2 += 100
            game.affiche_statut()
            for explose in explosions:
                explose.explode(arme_pl_2.xcor(), arme_pl_2.ycor())
        


        if player_2.is_collision(ally):
            # son
            os.system("afplay explosion.mp3&")
            game.lives_pl_2 -= 1
            player_2.goto(random.randint(-280,280), 280)
            player_2.speed = 0
            game.score_pl_2 -= 100
            game.affiche_statut()
            for explose in explosions:
                explose.explode(ally.xcor(), ally.ycor())
            # vie
            if game.lives_pl_2 <= 0:
                player_2.ht()
                game.state = "game_over"



    if detect_collision(player, player_2):
        x_pl_1 = random.randint(-280,280)
        y_pl_1 = -280
        x_pl_2 =  random.randint(-280,280)
        y_pl_2 = 280 
        # son
        os.system("afplay explosion.mp3&")
        game.lives -= 1
        game.lives_pl_2 -= 1
        for explose in explosions:
            explose.explode(player.xcor(), player.ycor())
        player.goto(random.randint(-280,280), -280)
        player_2.goto(random.randint(-280,280), 280)
        game.score -= 50
        game.score_pl_2 -= 50
        game.affiche_statut()
        # vie
        if game.lives <= 0:
            player.ht()
            game.state = "game_over"
        if game.lives_pl_2 <= 0:
            player_2.ht()
            game.state = "game_over"


    # player attack other player
    if arme_pl_1.is_collision(player_2):
        # son
        os.system("afplay explosion.mp3&")
        game.lives_pl_2 -= 1
        player_2.goto(random.randint(-280,280), 280)
        player_2.speed = 0
        arme_pl_1.status = "ready"
        game.score += 100
        game.affiche_statut()
        for explose in explosions:
            explose.explode(arme_pl_1.xcor(), arme_pl_1.ycor())

        # vie
        if game.lives_pl_2 <= 0:
            player_2.ht()
            game.state = "game_over"
    
    if arme_pl_2.is_collision(player):
        # son
        os.system("afplay explosion.mp3&")
        game.lives -= 1
        player.goto(random.randint(-280,280), -280)
        player.speed = 0
        arme_pl_2.status = "ready"
        game.score_pl_2 += 100
        game.affiche_statut()
        for explose in explosions:
            explose.explode(arme_pl_2.xcor(), arme_pl_2.ycor())
        
        # vie
        if game.lives <= 0:
            player.ht()
            game.state = "game_over"

    for explose in explosions:
        explose.move()

    if game.lives == 0:
        player.Arreter()
        player_2.Arreter()

        for ennemy in enemies:
            ennemy.Arreter()

        for ally in allies:
            ally.Arreter()

    if game.lives_pl_2 == 0:
        player.Arreter()
        player_2.Arreter()
        
        for ennemy in enemies:
            ennemy.Arreter()

        for ally in allies:
            ally.Arreter()

    if (game.lives == 0) & (game.lives_pl_2 == 0):
        player.Arreter()
        player_2.Arreter()
        
        for ennemy in enemies:
            ennemy.Arreter()

        for ally in allies:
            ally.Arreter()
 
    
#turtle.done()