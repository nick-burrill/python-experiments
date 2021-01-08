#needs to be ran in python 3 and up
import turtle
import time
import random
import math

nativefps = 60 #amount of frames if skipframe is false race is is usually 3 seconds long
skipframe= True #skip frames to make race duration the same
fps=60 #fps of turtle movement

window = turtle.Screen()
window.bgcolor("darkgrey")

jeff = turtle.Turtle()
jeff.shape("turtle")
jeff.color("darkgreen")
jeff.pencolor("black")


if skipframe == True:
	JS = (random.uniform(100 / fps, 130 / fps)) #jeff's speed

	while jeff.xcor() < 300:
		JS = (random.uniform(-3.219 / fps, 3 / fps) + JS)
		if JS < 90 / fps:
			JS = 90 / fps

		jeff.forward(JS)
		time.sleep(1/fps)
		print (JS)


if skipframe == False:
	JS = (random.uniform(100 / nativefps, 130 / nativefps)) #jeff's speed

	while jeff.xcor() < 300:
		JS = (random.uniform(-3.2 / nativefps, 3 / nativefps) + JS)
		if JS < 90 / nativefps:
			JS = 90 / nativefps

		jeff.forward(JS)
		time.sleep(1/fps)
		print (JS)


