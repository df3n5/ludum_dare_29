# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg hotel lobby = "lobby_bg.png"

image sq normal = "square.png"
image tri normal = "triangle.png"
image hex normal = "hexagon.png"
image ci normal = "circle.png"

# Declare characters used by this game.
#define e = Character('Jonathan', color="#c8ffc8")
#define m = Character('Aoife', color="#ffffff")
define s = Character('Square', color="#842a13") #Square
define t = Character('Triangle', color="#152dbd") #Triangle
define h = Character('Hexagon', color="#c69317") #Hexagon

define c = Character('Circle', color="#95ff87")

# The game starts here.
label start:
    $ guessed_correctly = False
    jump knightsknaves
    "What would you like to do?"
    menu:
        "Interrogate someone":
             jump interrogate
        "Accuse someone":
             jump accuse

label knightsknaves:
    scene bg hotel lobby
    show ci normal at left
    "You know one of Triangle, Square and Circle are lying."
    show sq normal at right
    c "Square, are you the liar?"
    s "*mumble*"
    hide sq
    show tri normal at right
    t "Square said that she is a liar. Is it a she?"
    c "I don't know, do squares have genders?"
    hide tri
    show sq normal at right
    s "Of course we do."
    s "Why would you think we didn't?"
    c "I don't know, this is my first time meeting straight shapes. Now Mr. Exa.."
    hide sq
    show tri normal at right
    t "Woah, woah, woah - call me straight one more time and see what happens!"
    c "Oh I'm sorry, I meant no offence. My grandfather was a semicircle!"
    hide tri
    show hex normal at right
    h "Don't worry about Triangle. He has something against round heads. You were asking something?"
    c "Oh yes, Mr. Hexagon is it? Do you know anything about the liar?"
    h "Triangle's answer was wrong. Don't believe him."
    jump knightsknaves_guess

label knightsknaves_guess:
    scene
    "Who is the liar?"
    menu:
        "Square":
             jump knightsknaves_failed
        "Triangle":
             jump knightsknaves_success
        "Hexagon":
             jump knightsknaves_failed
        "Hear it again":
             jump knightsknaves
    
label knightsknaves_failed:
    "Wrong, try again."
    jump knightsknaves_guess

label knightsknaves_success:
    "Correct!"
    scene bg hotel lobby
    show ci normal at left
    show tri normal at right
    c "So Triangle man, it was you who was lying?"
    t "When he's underwater does he get wet?"
    c "Eh, what?"
    t "Oh excuse me, yes that's correct. Well done to you."
    c "Okay then..."
    jump end

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
    "You have gotten the killer"
    $ guessed_correctly = True
    jump end

label accuse_square:
    "You have accused square of misdeeds"
    jump end

label accuse_circle:
    "You have accused circle of misdeeds"
    jump end

label end:
    scene black
    if guessed_correctly:
        "Tell the player the whole story"
    "THE END"

