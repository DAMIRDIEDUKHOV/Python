from turtle import *
exitonclick()

def background():  # Fix the typo in function name
    color('orange')
    penup()
    goto(-300, 300)
    pendown()
    begin_fill()
    for i in range(4):
        forward(800)
        right(90)
    end_fill()

def display_image():
    register_shape("image.png")  # Replace "image.png" with your actual image file
    img_turtle = Turtle()
    img_turtle.penup()
    img_turtle.shape("image.png")
    img_turtle.goto(0, -100)
    img_turtle.showturtle()

background()  # Call the corrected function name

color('black')
penup()
goto(0, 0)
write('Tell me what game I should make down in the', align="center", font=("Arial", 16, "normal"))

penup()
goto(0, -30)
write('comments section.', align='center', font=("Arial", 16, 'normal'))

hideturtle()

display_image()

done()