# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg hotel lobby = "lobby_bg.png"
image bg hotel bedroom = "bedroom_bg.png"

image sq normal = "square.png"
image tri normal = "triangle.png"
image hex normal = "hexagon.png"
image ci normal = "circle.png"
image oct normal = "octagon.png"

# Declare characters used by this game.
#define e = Character('Jonathan', color="#c8ffc8")
#define m = Character('Aoife', color="#ffffff")
define s = Character('Square', color="#842a13") #Square
define t = Character('Triangle', color="#152dbd") #Triangle
define h = Character('Hexagon', color="#c69317") #Hexagon

define o = Character('Sheriff Octagon', color="#52b4ff") #Octagon

define c = Character('Circle', color="#95ff87") #Circle

# The game starts here.
label start:
    $ guessed_correctly = False
    #jump act2
    jump act4
    "What would you like to do?"
    menu:
        "Interrogate someone":
             jump interrogate
        "Accuse someone":
             jump accuse

label act1:
    "Act 1"
    jump act2

label act2:
    scene
    "Act 2"
    jump knightsknaves

label knightsknaves:
    scene bg hotel lobby
    show ci normal at left
    with dissolve
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
    t "Oh excuse me. Well done to you."
    c "Okay then..."
    jump act3

label act3:
    scene
    "Act 3"
    "Circle gets his room key from the door and heads upstairs."
    "He decides to take a nap after his long journey."
    "Two hours later..."
    scene bg hotel bedroom
    show ci normal at left
    with dissolve
    "*Knock knock*"
    c "Who is it?"
    t "Hey it's me Triangle, there's an emergency in the lobby, let me in!"
    c "Eugh."
    "Circle unlocks the door"
    show tri normal at right
    c "So what's happened?"
    t "The receptionist has been stabbed!"
    t "Please come down to the lobby."
    t "The sheriff has asked me to round everyone up."
    c "Okay I'll get dressed. Let him know I'll be down soon"
    t "Okay I will go get Circle and Square."
    c "Are we the only people at this hotel?!"
    t "Yeah, it's pretty quiet."
    c "Jesus"

    scene bg hotel lobby
    show oct normal at left
    show ci normal at right
    with dissolve

    o "It appears like we are all here now."
    o "I hear you are an investigator?"
    c "Yeah, I am a special agent for the FBI."
    "Circle shows his badge to Sheriff Octagon"
    c "This is my first time off in 2 years."
    o "What a coincidence, this is my first day as a policeman."
    c "On your first day you were made Sheriff?"
    o "Sheriffs here don't seem to last very long."
    o "The last one gave me this shirt before he died."
    c "Oh so he was an Octagon as well?"
    o "No he was a rectangle."
    c "I see."
    o "Listen Circle"
    o "I've looked around and I can't find any evidence which might lead us to the killer."
    o "All I know is that it was one of Square, Triangle and Hexagon."
    o "And that 2 of them have a pact to lie in response to any questioning."
    o "But the other one will always tell the truth"
    o "I've never questioned anyone before. Could you help me out in finding out who the killer is?"
    c "Eugh, I guess crime doesn't take a holiday."
    c "Okay fine. Let's do this."
    scene
    jump act4
    
label act4:
    scene bg hotel lobby
    show ci normal at left
    "Act 4"

    "What would you like to do?"
    menu:
        "Interrogate someone":
             jump interrogate
        "Accuse someone":
             jump accuse
        "Summary of situation":
             jump summary 

label summary:
    "One of Square, Triangle and Hexagon is the killer."
    "2 of them have a pact to lie in response to any questioning."
    "The other one will always tell the truth."
    "Can you find the killer?"
    jump act4

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

