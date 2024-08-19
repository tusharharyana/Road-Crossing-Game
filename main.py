#Road crossing game
#@tusharharyana

import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

#To start game again.
def reset_game():
    global player, scoreboard, car_manager, game_is_on
    screen.clear()
    screen.tracer(0)
    
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    game_is_on = True
    
    screen.listen()
    screen.onkey(player.go_up,"Up")
    

def game_over():
    global game_is_on
    scoreboard.game_over()
    screen.update()
    time.sleep(0.5) #Pause for a moment to display the game over message.
    
    #Prompt user to play again.
    
    response = screen.textinput("Game Over", "Do you want to play again? (Yes/No)").lower()
    if response == "yes":  
        reset_game()
    else:
        screen.bye()

    
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Road Crossing Game")
screen.tracer(0)

reset_game() #Initilize the game.


while True:
    if game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()
        
        #Detect collision with cars
        
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                game_over()
                
        
        #Detect sucessfull crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
    else:
        game_over()

screen.mainloop()
# screen.exitonclick()