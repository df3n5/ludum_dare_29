# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Jonathan', color="#c8ffc8")
define m = Character('Aoife', color="#ffffff")
    

# The game starts here.
label start:
    "What would you like to do?"
    
menu:
    "Interrogate someone":
         jump vn
    "Accuse someone":
         jump hentai

label vn:
    m "It's a story with pictures and music."
    jump marry

label hentai:
    m "Why it's a game with lots of sex."
    jump marry

label marry:
    scene black
    with dissolve

    "--- years later ---"

