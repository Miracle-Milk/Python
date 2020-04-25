
import turtle       ##导入
import random       ##随机返回一个0到1之间的实数

##function
def screenLeftClick(x,y):   ##按下鼠标左键
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):  ##右键
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()

##变量声明
pSize =10
r,g,b=0.0,0.0,0.0

##main code
turtle.title('turtle graphics')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()