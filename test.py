from turtle import Turtle, Screen
sam = Turtle()
window = Screen()
sam.shape("turtle")
sam.color("white")
window.bgcolor("black")
sam.hideturtle()
sam.write("Welcome👋",align="center",font=("Arial",25,"normal"))
window.exitonclick()