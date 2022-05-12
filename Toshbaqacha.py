from turtle import Turtle, Screen
import turtle

def function1():
    toshbaqa.forward(50)

def function2():
    toshbaqa.left(50)

def function3():
    toshbaqa.right(50)

def function4():
    root.bye()

def function5():
    toshbaqa.back(50)

def function6():
    toshbaqa.forward(100)

def function7():
    toshbaqa.clone()

root = Screen()

root.bgcolor('lightgreen')

root.title('Toshbaqacha')

root.onkey(function1, 'Up')
root.onkey(function2, 'Left')
root.onkey(function3, 'Right')
root.onkey(function4, 'q')
root.onkey(function5, 'Down')
root.onkey(function6, 'v')
root.onkey(function7, 'n')

toshbaqa = Turtle()
toshbaqa.shape('turtle')
toshbaqa.color('darkgreen')


root.listen()
root.mainloop()