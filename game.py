import os
from enum import Enum

class End(Enum):
     GOOD = 1
     BAD = 0

#Every time a event gets success or failed then its added into this dictionary so it can easily be accessed later in the game when we need to call them
#the dict works like this the key is the name of the of the character + the event and True/False whether it succeeded or not
eventSuccess = { "kanndyEvent1": True , "kanndyevent2": False }

characterDirectory = "Character"

def execScript(characterName, scriptName, extract=[]):
    _locals = locals()
    exec(open(
        os.path.join(
            characterDirectory,
            characterName,
            scriptName
        )
    ).read(), globals(), _locals)
    return [_locals[var] for var in extract]


def callEvent(characterName, eventName, number, cli=False):
    eventClimax = execScript(characterName, "event{}{}.py".format("Cli" if cli else "", number), ["eventClimax"])[0]
    eventSuccess[eventName] = eventClimax

def callEnd(characterName, endtype):
    if endtype == End.GOOD:
        execScript(characterName, "goodEnd.py")
    elif endtype == End.BAD:
        execScript(characterName, "badEnd.py")

print(eventSuccess['eventTest'])
