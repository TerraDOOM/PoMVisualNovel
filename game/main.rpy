init python:
    import os

    # Every time a event gets success or failed then its added into this
    # dictionary so it can easily be accessed later in the game when we need to call them.
    #
    # the dict works like this:
    # the key is the name of the of the character + the event and True/False whether it succeeded or not
    eventSuccess = {} # Example: { "kanndyevent1": True , "kanndyeventCli2": False }
     
    characterDirectory = "Character" # Name for the character directory
     
    GOOD_END = "good"
    BAD_END = "bad"
     
    def execScript(characterName, scriptName, extract=[]):
        """
        Call any character script, this is what both callEvent and callEnd uses internally
     
        characterName: the name of the character that has the script
        scriptName: the script that we wish to execute
        extract: an array of variable names that we wish to extract out of the script execution, can be empty if we don't want anything
        """
        to_extract = {} # make an empty "namespace"
        exec(open(
                # using os.path.join to make sure we get correct behaviour regardless of OS
                os.path.join(
                    characterDirectory,
                    characterName,
                    scriptName + ".py"
                    )
                ).read(), [], to_extract) # read in the file, then hand it an empty local namespace that it can fill.
        return [to_extract[var] for var in extract] # return every local variable from script execution that was mentioned in extract
     
    def callEvent(characterName, number, cli=False):
        """
        Call a specific character's event
     
        characterName: name of the character that has the event
        number: which number the event is (must be 1-6, inclusive), NOTE: this can only be 1 or 2 if it's a cli event.
        cli: whether the event is a climax or not (default: False)
        """
        assert 1 <= number <= 6, "event number was outside the range [1, 6]"
        scriptName = "event{}{}".format("Cli" if cli else "", number)
        eventClimax = execScript(characterName, scriptName, ["eventClimax"])[0]
        eventSuccess[characterName + scriptName] = eventClimax
     
    def callEnd(characterName, endType):
        """
         Call a specific character's ending
         
         characterName: the character's name
         endType: the type of ending (good/bad). Use the constants GOOD_END and BAD_END to specify endType please
         """
        execScript(characterName, "{}End".format(endType))
