import turtle


#it plots the screen
window = turtle.Screen()
window.bgcolor("red")

#it creates the cursor and relevant movements
k = turtle.Turtle()
k.shape("turtle")
k.color("black")
k.speed(5)

#moves forward - by default towards right
k.forward(100)
#takes the angle on right of 90 degrees
k.right(90)
k.forward(100)
k.right(90)
k.forward(100)
k.right(90)
k.forward(100)
k.right(90)

window.exitonclick()
