import time
import turtle
from turtle import *

wn = turtle.Screen()
Resultant_Matrix = []
colormode(255)

#Used to draw lines on screen
def lines():
    speed(.5)
    color('black')
    for i in range(15):
        pu()
        goto(-7 + i, -7)
        pd()
        goto(-7 + i, 7)
        pu()
    for j in range(15):
        pu()
        goto(-7, -7 + j)
        pd()
        goto(7, -7 + j)
        pu()


# draw x and y axis
def setup():
    # "draw the x-y grid"
    speed(0)
    setworldcoordinates(-7, -7, 7, 7)
    setpos(0, 0)
    clear()
    lines()
    setpos(0, 0)
    setheading(0)  # faces the right of the screen
    pd()
    color('black')
    for i in range(4):
        setpos(0, 0)
        fd(7)
        rt(90)
    pu()


# Matrix representation of L
Lmatrix = [[0, 0],
           [1, 0],
           [2, 0],
           [3, 0],
           [3, 1],
           [1, 1],
           [1, 6],
           [0, 6],
           [0, 0]]

#Connect the point in matrix of L with a line
def drawL(MatrixL):
    pu()
    goto(0, 0)
    pd()
    for point in MatrixL:
        pensize(5)
        goto(point[0], point[1])

#Multiply the matrix L with a 2*2 transformation matrix
def matMul(a, b):
    Resultant_Matrixrix = []
    for i in range(len(a)):
        Resultant_Matrixrix.append([])
        for j in range(2):
            Resultant_Matrixrix[i].append(a[i][0] * b[0][j] + a[i][1] * b[1][j])
    return Resultant_Matrixrix

#Used to set the name of the screen and calls drawL function
def draw(nameOfOperation, Mat, MatL):
    pensize(1)
    wn.title(nameOfOperation)
    time.sleep(5)
    tracer(2)
    clear()
    setup()
    pensize(2)
    color('blue')
    drawL(MatL)
    color('red')
    drawL(Mat)


# transformation matrix
same = [[1, 1],
        [1, 1]]
x_reflection = [[1, 0],
               [0, -1]]
y_reflection = [[-1, 0],
               [0, 1]]
counter_clockwise_90= [[0, 1],
               [-1, 0]]
clockwise_90 = [[0, -1],
                [1, 0]]

#Letter L

tracer(1.5)
setup()
color('red')
wn.title("Letter L")
drawL(Lmatrix)

#x-reflection
Resultant_Matrix = matMul(Lmatrix, x_reflection)
draw("Reflection along x-axis",Resultant_Matrix, Lmatrix)

#y-reflection
Resultant_Matrix = matMul(Lmatrix, y_reflection)
draw("Reflection along y-axis", Resultant_Matrix, Lmatrix)

#clockwise-90
Resultant_Matrix = matMul(Lmatrix, clockwise_90)
draw("Clockwise rotation by 90", Resultant_Matrix, Lmatrix)

#counter_clockwise_90
Resultant_Matrix = matMul(Lmatrix, counter_clockwise_90)
draw("Counter clockwise rotation by 90" ,Resultant_Matrix, Lmatrix)

wn.tracer(2)
wn.exitonclick()


