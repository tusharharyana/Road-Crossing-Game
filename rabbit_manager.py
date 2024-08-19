from turtle import Turtle,Screen
import random

COLORS = ["red", "yellow", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class RabbitManager:
    
    def __init__(self):
        self.all_rabbit = []
        self.rabbit_speed = STARTING_MOVE_DISTANCE
        
        screen = Screen()
        screen.register_shape("rabbitGif/rabbit.gif") 
        
    def create_rabbit(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_rabbit = Turtle()
            new_rabbit.shape("rabbitGif/rabbit.gif")
            # new_rabbit.shapesize(stretch_wid=1,stretch_len=2)
            new_rabbit.penup()
            new_rabbit.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_rabbit.goto(300,random_y)
            self.all_rabbit.append(new_rabbit)
        
    def move_rabbit(self):
        for rabbit in self.all_rabbit:
            rabbit.backward(self.rabbit_speed)
            
    def level_up(self):
        self.rabbit_speed += MOVE_INCREMENT