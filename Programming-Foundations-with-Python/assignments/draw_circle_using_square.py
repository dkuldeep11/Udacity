import turtle


def draw_square(t1):
  for i in range(4):
    t1.forward(100)
    t1.right(90)

#it plots the screen
window = turtle.Screen()
window.bgcolor("red")

#it creates the cursor and relevant movements
k = turtle.Turtle()
k.shape("turtle")
k.color("black")
k.speed(5)
draw_square(k)

#draw circle
for i in range(36):
  draw_square(k)
  k.right(10) 


window.exitonclick()
