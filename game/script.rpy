# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#define e = Character('Jonathan', color="#c8ffc8")
#define m = Character('Aoife', color="#ffffff")
    

# The game starts here.
label start:
    "What would you like to do?"
    menu:
        "Interrogate someone":
             jump interrogate
        "Accuse someone":
             jump accuse

label interrogate:
    "You decide to interrogate someone"
    jump end

label accuse:
    "Who do you want to accuse?"
    jump end

label end:
    scene black
    "THE END"
