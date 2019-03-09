import os
from enum import Enum

class End(Enum):
     GOOD = 1
     BAD = 0

#Every time a event gets success or failed then its added into this dictionary so it can easily be accessed later in the game when we need to call them
#the dict works like this the key is the name of the of the character + the event and True/False whether it succeeded or not
eventSuccess = { "kanndyEvent1": True , "kanndyevent2": False }

characterDirectory = "Character" # Name for the character directory


def execScript(characterName, scriptName, extract=[]):
     """
     Call any character script, this is what both callEvent and callEnd uses internally

     characterName: the name of the character that has the script
     scriptName: the script that we wish to execute
     extract: an array of variable names that we wish to extract out of the script execution, can be empty if we don't want anything
     """
     _locals = locals() # get a copy of the local namespace
     exec(open(
          # using os.path.join to make sure we get correct behaviour regardless of OS
          os.path.join(
               characterDirectory,
               characterName,
               scriptName
          )
     ).read(), globals(), _locals) # read in the file, then hand it the local namespace. No idea why we need to do this, and it's probably a bad idea, but it works
     return [_locals[var] for var in extract] # return every local variable from script execution that was mentioned in extract


def callEvent(characterName, number, cli=False):
     """
     Call a specific character's event

     characterName: name of the character that has the event
     number: which number the event is (must be 1-6, inclusive)
     cli: whether the event is a climax or not (default: False)
     """
     assert(1 <= number <= 6, "event number was outside the range [1, 6]")
     scriptName = "event{}{}.py".format("Cli" if cli else "", number)
     eventClimax = execScript(characterName, scriptName, ["eventClimax"])[0]
     eventSuccess[characterName + scriptName] = eventClimax

def callEnd(characterName, endtype):
     """
     Call a specific character's ending

     characterName: the character's name
     endtype: the type of ending (good/bad). Use the `End` enum for this.
     """
     if endtype == End.GOOD:
          execScript(characterName, "goodEnd.py")
     elif endtype == End.BAD:
          execScript(characterName, "badEnd.py")

print(eventSuccess['eventTest'])
