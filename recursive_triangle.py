from turtle import Turtle
import math
import random

def recursive_spiral(turtle, side_len, angle, scalefactor, min_len):
    colors = ["red", "orange", "blue", "purple"]
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(side_len)
    turtle.left(angle)
    side_len = side_len * scalefactor
    if (side_len > min_len):
        recursive_spiral(turtle, side_len, angle, scalefactor, min_len)

def main():
    animation_speed = 0
    michelangelo = Turtle()
    michelangelo.speed(animation_speed)
    recursive_spiral(michelangelo, 320, 121, 0.98, 15
                     )

main()
