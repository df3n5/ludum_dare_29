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

# Interrogations
label interrogate:
    "Who do you want to interrogate?"
    menu:
        "Triangle":
             jump interrogate_triangle
        "Square":
             jump interrogate_square
        "Circle":
             jump interrogate_circle

label interrogate_triangle:
    "You have interrogated triangle of misdeeds"
    jump end

label interrogate_square:
    "You have interrogated square of misdeeds"
    jump end

label interrogate_circle:
    "You have interrogated circle of misdeeds"
    jump end

# Accusations
label accuse:
    "Who do you want to accuse?"
    menu:
        "Triangle":
             jump accuse_triangle
        "Square":
             jump accuse_square
        "Circle":
             jump accuse_circle

label accuse_triangle:
    "You have accused triangle of misdeeds"
    jump end

label accuse_square:
    "You have accused square of misdeeds"
    jump end

label accuse_circle:
    "You have accused circle of misdeeds"
    jump end

label end:
    scene black
    "THE END"
