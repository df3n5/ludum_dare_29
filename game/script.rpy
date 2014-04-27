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
    jump act1
    "What would you like to do?"
    menu:
        "Interrogate someone":
             jump interrogate
        "Accuse someone":
             jump accuse

label act1:
    scene black with dissolve
    show text "Act 1" with Pause(1.5)
    scene black with dissolve
    jump act2
    scene bg hotel lobby
    show ci normal at left
    with dissolve
    c "Finally, my holiday can start."
    c "I am going to soak up so much sun and drink so much alcohol."
    c "Maybe I'll get a nice scotch. It's been so long since I've had a drink."
    show sq normal at right
    s "Oh hi there"
    c "Uh"
    c "Hello."
    s "Would you like to play a game?"
    c "Em not really, I haven't checked in yet. Please excuse me."
    s "I'm afraid I'm going to have to not excuse you. I'm on holiday with my two friends and they are driving me insane."
    s "You will play, or ..."
    c "Fine, fine."
    s "Super!"

label act2:
    scene
    scene black with dissolve
    show text "Act 2" with Pause(1.5)
    scene black with dissolve
    s "Okay let's play Knight's and Knaves"
    jump knightsknaves

label knightsknaves:
    scene bg hotel lobby
    show ci normal at left
    with dissolve
    show sq normal at right
    s "You know one of the three of us is lying."
    s "But the other two will always tell the truth"
    c "Okay fine."
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
    c "I don't know, this is my first time meeting straight shapes. Now Mr. Hexa.."
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
    c "I'm leaving now"
    jump act3

label act3:
    scene
    scene black with dissolve
    show text "Act 3" with Pause(1.5)
    scene black with dissolve
    "Circle gets his room key from the door and heads to his room."
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
    c "This is my first time off in two years."
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
    o "And that two of them have a pact to lie in response to any questioning."
    o "But the other one will always tell the truth"
    o "I've never questioned anyone before. Could you help me out in finding out who the killer is?"
    c "Eugh, I guess crime doesn't take a holiday."
    c "Okay fine. Let's do this."
    scene
    jump act4_start
    
label act4_start:
    scene black with dissolve
    show text "Act 4" with Pause(1.5)
    scene black with dissolve
    jump act4

label act4:
    scene bg hotel lobby
    show ci normal at left

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
    "Two of them have a pact to lie in response to any questioning."
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
        "Hexagon":
             jump interrogate_hexagon

label interrogate_triangle:
    "You have decided to interrogate Triangle"
    scene bg hotel lobby
    show ci normal at left
    show tri normal at right
    "What would you like to ask?"
    menu:
        "What is your story?":
            t "What do you want to know about me?"
            c "How about where did you grow up?"
            t "These questions are stupid."
            t "*Sigh* I grew up on a submarine with Square and Circle."
            t "We are all brothers you see."
            t "Our father was an ex-submarine commander who was given a dishonourable discharge."
            t "So one night when docked he brought us and our mother on board the submarine."
            t "He kicked all of the remaining crew out and hijacked the submarine."
            t "Ever since then we have lived at sea."
            t "Our parents died years ago, but we still take care of the submarine."
            t "We're here on holiday from it all - there's only so long you can stay below sea level before you go crazy."
            c "Right..."
            jump interrogate_triangle
        "Have you ever killed anyone?":
            t "Hundreds."
            t "It's a necessary price to pay when you are on the run from the law."
            t "If someone catches you, you can't let them escape."
            c "Right."
            jump interrogate_triangle
        "Did you kill the receptionist?":
            t "Yes, fine I did it."
            t "That's what you want me to say isn't it?"
            t "Well it's true."
            t "Triangle Man hates Person man,"
            t "They have a fight, Triangle wins,"
            t "Triangle man."
            t "Triangle always wins"
            c "..."
            c "Thank you Mr Triangle."
            jump interrogate_triangle
        "Go back":
            jump act4

label interrogate_square:
    "You have decided to interrogate Square"
    scene bg hotel lobby
    show ci normal at left
    show sq normal at right
    "What would you like to ask?"
    menu:
        "What is your story?":
            s "The contents of my life are quite inconsequential."
            t "Okay, can you at least tell me how you came to be here?"
            s "Oh yeah sure, I'm with my friends Circle and Triangle on holiday like you."
            t "And how long have you been friends?"
            s "Forever, I mean since we were really young."
            s "We went to the same school, and have hung around ever since."
            jump interrogate_square
        "Have you ever killed anyone?":
            s "I'm not proud of it but yes."
            t "Can you tell me anymore about that?"
            s "Not that I feel like right now."
            jump interrogate_square
        "Did you kill the receptionist?":
            s "Yes, it was me okay."
            c "You killed the receptionist?"
            s "Yes I killed her."
            jump interrogate_square
        "Go back":
            jump act4

label interrogate_hexagon:
    "You have decided to interrogate Hexagon"
    scene bg hotel lobby
    show ci normal at left
    show hex normal at right
    "What would you like to ask?"
    menu:
        "What is your story?":
            h "My parents were killed when I was 12."
            h "I was raised by my abusive uncle Curvilinear Triangle."
            h "When I turned 18, I turned to drink and drugs - fuelled by the money my parents left me."
            h "After that my life went into a downhill spiral until I lost all of my money and roamed the streets."
            h "I ended up in prison for manslaughter."
            h "During my stay in prison I found God."
            h "I have repented for my sins and live a good clean life now."
            h "I am here with these men on a religious retreat."
            h "But tell me, have you found faith in the Lord our saviour?"
            c "Eh no, but thanks."
            jump interrogate_hexagon
        "Have you ever killed anyone?":
            h "Well..."
            h "I did kill some people in the past."
            h "But I've done my time in prison."
            h "Your hair is pretty."
            c "Eh, okay thanks."
            jump interrogate_hexagon
        "Did you kill the receptionist?":
            h "It was Triangle who killed the receptionist."
            h "I was taking a walk outside by the lake and I saw him do it through the window."
            h "His 60 degree angles are unmistakeable."
            h "Please take him away, I don't want anything to do with him anymore."
            c "Thank you Mr. Hexagon"
            jump interrogate_hexagon
        "Go back":
            jump act4

# Accusations
label accuse:
    "Who do you want to accuse?"
    menu:
        "Triangle":
             jump accuse_triangle
        "Square":
             jump accuse_square
        "Hexagon":
             jump accuse_hexagon

label accuse_triangle:
    "You have accused Triangle of misdeeds"
    "You have guessed incorrectly!"
    jump act4

label accuse_square:
    "You have accused Square of misdeeds"
    "You have gotten the killer!"
    $ guessed_correctly = True
    jump act5

label accuse_hexagon:
    "You have accused Hexagon of misdeeds"
    "You have guessed incorrectly!"
    jump act4

label act5:
    scene black with dissolve
    show text "Act 5" with Pause(1.5)
    scene black with dissolve

    scene bg hotel lobby
    show ci normal at left
    show sq normal at right
    c "So, Square it was you all along!"
    s "Damn it, how did you figure it out?"
    c "Well I knew two of you were lying, and one was telling the truth."
    s "Kay"
    c "When Hexagon said it was Triangle, I knew that couldn't be true."
    c "Since if he was telling the truth, then both you and Triangle had to be lying, which cannot happen since both of you said you did it."
    c "So Hexagon must be a liar, which makes Triangle a liar too since his testimony was the same as yours."
    c "So that only leaves one person - "
    s "My head hurts - fine you have got me. Damn these rules!"

    scene bg hotel lobby
    show oct normal at left
    show sq normal at right
    o "I'm going to lock you up for a long time Square."
    s "Oh I'm scared, my friends will come after you with a submarine"
    o "That never actually happened Square."
    s "Oh yeah. God damn it."
    h "How dare you take the Lord's name in vain!"
    s "You're not really a born again Christian Hexagon. You're both terrible liars."
    o "That's enough"

    scene bg hotel lobby
    show oct normal at left
    show ci normal at right
    o "Thanks for your help Circle. That Square is off the streets now."
    c "Okay fine, now please just leave me alone for the rest of my trip"
    o "Okay no problem"

    scene bg hotel lobby
    show ci normal at left
    show tri normal at right
    t "So you have to spend the rest of your trip with us?"
    c "Yeah, you the two liars or the murderer. It was a hard decision."
    h "So." 
    t "This is awkward."
    h "Do you want to play a game?"
    t "Yeah! Let's play Knights and Knaves!"
    h "Yay!"
    c "Eugh"
    jump end


label end:
    scene black with dissolve
    show text "The End" with Pause(1.5)
    scene black with dissolve

    scene black with dissolve
    show text "A game for Ludum Dare 29 by Jonathan Frawley" with Pause(1.5)
    scene black with dissolve

    scene black with dissolve
    show text "Made with Renpy and gimp in 48 hours." with Pause(1.5)
    scene black with dissolve

    scene black with dissolve
    show text "Thanks for playing!" with Pause(1.5)
    scene black with dissolve
    
    jump start
