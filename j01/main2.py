import turtle
import random

def tree(branchLen, t, deep=6):
    if deep == 0:
        return
    
    save_color = t.pencolor()
    save_size = t.pensize()

    t.color((0, 0.15+(0.75**deep), 0))
    t.pensize(10*deep*0.75)
          
    t.forward(branchLen)
    t.right(20)
    
    k = random.gauss(0, branchLen/4)
    
    tree(branchLen * 0.75 + k, t, deep-1)

    t.left(40)

    tree(branchLen*0.75 + k, t, deep-1) 

    t.right(20)
    t.backward(branchLen)

    t.color(save_color)
    t.pensize(save_size)

def main():
    t = turtle.Turtle()

    myWin = turtle.Screen()

    t.color((0, 0.15, 0))
    t.pensize(10)

    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    s = input("Вкажіть глибину рекурсії [6]")
    if s and s.isnumeric():
        N = int(s)
    else:
        N = 6
    

    tree(100, t)

    myWin.exitonclick() 