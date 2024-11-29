import turtle
import arabic_reshaper
import pandas
from bidi.algorithm import get_display

# Screen set up
screen = turtle.Screen()
screen.title("Palestine Villages Game")
image = "Blank_Palestine_Map.gif"
screen.addshape(image)
turtle.shape(image)

# Data set up
data = pandas.read_csv("16_villages.csv")

# Prompt
text = 'أدخل اسم مدن فلسطينية'
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

# Turtle setup
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()
FONT = ("courier", 8, "normal")



# Game
count = 0
guessedVillages = []
villagesToLearn = []
villages = data.village.to_list()
while count<len(villages):
    answer = screen.textinput(title=f"Guessed {count}/16", prompt=bidi_text)
    
    if answer == "ساعدني" or answer == "مساعدة":
        for village in villages:
             if village not in guessedVillages:
                villagesToLearn.append(village)
                dataFrame = pandas.DataFrame(villagesToLearn)
                dataFrame.to_csv("VillagesToLearn")
        break
    
    if (answer in villages) and (answer not in guessedVillages):
            guessedVillages.append(answer)
            count += 1
            row = data[data.village == answer]
            x = row.x.item()
            y = row.y.item()
            cursor.goto((x,y))
            cursor.write(answer, font=FONT)

if count==16:
    cursor.goto(-100,200)
    cursor.color("green")
    cursor.write("!لقد فزت", font=FONT)

screen.exitonclick()
