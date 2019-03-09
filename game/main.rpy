# list of characters:
# Cassandra
# Cindy
# Inori
# Ira
# Kanndy
# Lily

define me = Character("[playername]")
define cindy = Character("Cindy")
define msbelle = Character("Ms. Belle")

image player room = "player room.png"
image phone clock late = "phone clock late.png"
image school grounds = "school grounds.png"
image classroom = "classroom.png"
image cindy = "cindy.png"

init python:
    # Every time a event gets success or failed then its added into this
    # dictionary so it can easily be accessed later in the game when we need to call them.
    #
    # the dict works like this:
    # the key is the name of the of the character + the event and True/False whether it succeeded or not
    eventSuccess = {} # Example: { "kanndyevent1": True , "kanndyeventCli2": False }

label start:
    $ playername = "Me"

    play sound "birds_chirping.ogg"

    "{i}Birds chirping{/i}"

    scene player room
    with fade

    "Huh? This isn't my bedroom?"

    "..."

    "Oh, that's right, this is my dorm in the university"

    "{i}yawn{/i} I wonder what time it is"

    show phone clock late at truecenter

    "..."

    "OH SHIT"

    "FUCK FUCK FUCK"

    "I'M LATE ON MY FIRST FUCKING DAY!"

    "I'VE SEEN HUNDREDS OF ANIME SHOWS WITH THIS EXACT SAME SCENARIO, AND I NEVER LEARN!!"

    scene school grounds
    with fade

    "Fuck I gotta run faster if I wanna make it in time!"

    "Wait, shit, I'm about to run into someone!"

    show cindy

    cindy "Ahh! Hey! Watch it you loser! You almost got your dumb peasant dirt all over me!"

    me "Sorry! Sorry! I'm late for class!"

    cindy "I don't care what your late for, loser! I would've had your ass arrested on the spot if you so much as touched me!"

    me "I'm sorry, okay!? I gotta go!"

    scene classroom
    with fade

    msbelle "You're late on your first day, doesn't give a good impression you know"

    msbelle "Alright, in any case, why don't you introduce yourself to the class"

    msbelle "Just tell everyone your name to begin with"

    python:
        playername = renpy.input("What's your name?")
        playername = playername.strip()

    me "Hello everyone, my name is [playername]! Happy to meet you all!"

    msbelle "You were late but since it's just your first day, I'll let it slide this time. I'll promptly punish you if you're late again!
             Almost all the seats are taken for now, but there's one left between Kanndy and Inori. So for the rest of term, you'll be sitting there. Now please be seated!"
