#UI Game 2
import pygame
import time
import random

pygame.init()

display_width=1024

display_height=768

black=(0,0,0)  #Using RGB. 

white=(255,255,255) #Using 255 instead of 256 becuase out of all the combinations, the absence of the parameter (i.e. 0) is one of them. So that leaves us with 255 "colors".

red=(255,0,0)

green=(0,255,0)

blue=(0,0,255)

yellow=(255,154,1)

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("The first car game!")

clock=pygame.time.Clock()

britcar_Img=pygame.image.load("car1.png")

def things(st_x,st_y,st_w,st_h,color):
	pygame.draw.rect(gameDisplay, color, [st_x,st_y,st_w,st_h])

def car(x,y):
	gameDisplay.blit(britcar_Img,(x,y))

def text_obj(stuff1,stuff2,col):
	textSurface=stuff2.render(stuff1,True,col)
	return textSurface, textSurface.get_rect()

def message_user(text):
	bigText=pygame.font.Font("freesansbold.ttf",120)
	TextSurf, TextRect =text_obj(text, bigText,white)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	time.sleep(3)
	pygame.display.flip()
	game_loop()

def dump():
	message_user("TRASHED!")

def game_loop():

	x=(display_width*0.45)
	y=(display_height*0.8)

	x_change=0
	y_change=0

	thing_startx=random.randrange(0,display_width)
	thing_starty=-600

	thing_vel=7

	thing_width=75
	thing_height=75
	car_width=171
	car_height=310

	crashed=False
	
	while not crashed:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				pygame.quit()
				quit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-8
			elif event.key==pygame.K_RIGHT:
				x_change=8
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				x_change=0	
		x+=x_change
		
		gameDisplay.blit(pygame.image.load("bg.jpg"),(0,0))
		
		things(thing_startx,thing_starty,thing_width,thing_height,red)
		thing_starty+=thing_vel
		#pygame.draw.rect(gameDisplay, yellow , [450,384,50,150])

		car(x,y)
		if x> display_width - car_width or x<0:
			dump()
		
		if thing_starty>display_height:
			thing_starty=-int(thing_height)
			thing_startx=random.randrange(0,display_width)
		
		if y<thing_starty+thing_height:
			if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
				dump()	

		pygame.display.flip()
		clock.tick(60)

file="slfctrl.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

game_loop()

pygame.quit()
quit()