#import any libraries we might need here
#pygame is a library that has some functions for making games
import pygame
#The GPIOZero library makes controlling our motionsensor easy
from gpiozero import MotionSensor
#This is the audo player - on RPi, try to use *.ogg NOT *.mp3 - I've had some issues using *.mp3s
from pygame import mixer
#Pseudo-random number for the green light phase
from random import *
#the Time module will help us count our sleepy naps, for when we want to pause our programme
import time

# activate the pygame library
# # initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

black = (0, 0, 0)

# assigning values to X and Y variable - this is how big our PyGame window is
X = 1920
Y = 1080

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
# set the pygame window name
pygame.display.set_caption('Red Light, Green Light')

#assign a pin to the sensor and give this an easy name (assign to a variable), in this case it is pin 4
pir = MotionSensor(4)

def game_intro():    

    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("musicbg.ogg")
    # Setting the volume
    mixer.music.set_volume(0.5)
    # Start playing the song
    mixer.music.play(1)
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'rgHome.png')
    # completely fill the surface object
    # with white colour
    display_surface.fill(black)
        
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))    

    # Draws the surface object to the screen.  
    pygame.display.update()
     
    # infinite loop
    gameIntro = True
    
    while gameIntro:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get() :
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
           if event.type == pygame.QUIT :
              # deactivates the pygame library
              pygame.quit()
              # quit the program.
              quit()
           #Press any key to start the game
           if event.type == pygame.KEYDOWN:
                startGame()

def startGame():
    
    # completely fill the surface object
    # with white colour
    display_surface.fill(black)
   
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'youwillbeplaying.png')     
   
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # Draws the surface object to the screen.  
    pygame.display.update()
    
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("YouWillBePlaying.ogg")
    # Setting the volume
    mixer.music.set_volume(0.5)
    # Start playing the song
    mixer.music.play(1)            
    #Have a little rest for 3 seconds
    time.sleep(3)
    #go to green light function
    greenLight()
  
   
   
def greenLight():
    #greenLightPhase
    
    ##Generate a random time length between 10 and 90 seconds
    Timer=randint(1,10)
    
    #this variable will act as a countdown timer
    time_left = Timer
         
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("GL.ogg")
    # Setting the volume
    mixer.music.set_volume(0.5)
    # Start playing the song
    mixer.music.play()
        
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'GL.png')
    # completely fill the surface object
    # with white colour
    display_surface.fill(black)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # Draws the surface object to the screen.  
    pygame.display.update()

    
    #This loop checks every second to see if any key on the keyboard has been pressed.
    #If a key is pressed, the player wins
    #Else after the set number of seconds, go to the red light phase
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                winner()
        time_left-=1
        if time_left>-1:
            time.sleep(1)
        else:
            redLight()


def redLight():
    
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("RL.ogg")
    # Setting the volume
    mixer.music.set_volume(0.5)
    # Start playing the song
    mixer.music.play()
     
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'RL.png')
    # completely fill the surface object
    # with white colour
    display_surface.fill(black)
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))
    # Draws the surface object to the screen.
    pygame.display.update()
    
    #IF loop to check for motion - if Motion detected, then go to playerDead else back to green light. timeout for PIR is set at (3)
    if pir.wait_for_motion(3):
        playerDead()
    else:
        greenLight()

def winner():
    
    # completely fill the surface object
    # with white colour
        display_surface.fill(black)
   
    # create a surface object, image is drawn on it.
        image = pygame.image.load(r'winner.png')     
   
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))
    
    # Draws the surface object to the screen.    
        pygame.display.update()
    #have a little sleepy for 3 seconds    
        time.sleep(3)
    #Go to the game intro screen    
        game_intro()

def playerDead():
    
    # completely fill the surface object
    # with white colour
        display_surface.fill(black)
   
    # create a surface object, image is drawn on it.
        image = pygame.image.load(r'dead.png')     
   
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))

        pygame.display.update()
    # Starting the mixer
        mixer.init()
    # Loading the song
        mixer.music.load("dead.ogg")
    # Setting the volume
        mixer.music.set_volume(0.5)
    # Start playing the song
        mixer.music.play(1)
    #Have a little sleepy for 3 seconds    
        time.sleep(3)
    #Go back to the intro
        game_intro()

#When we run our program, it will start with the game_intro() function that we created
game_intro()



 