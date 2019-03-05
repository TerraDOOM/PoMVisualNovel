#this class calls a file named after the character that is passed trough the constructor and then it goes into the files and find a directory named like the character and calls every event it needs from there
class Student:

    def __init__(self,name):
        import sys
        self.name = name
        sys.path.insert(0, 'Character/'+self.name)
        print("object created")

    def event1(self):
        import event1
        return event1.eventClimax

    def event2():
        import event2
        return event2.eventClimax
    def event3():
        import event3
        return event3.eventClimax
    def event4():
        import event4
        return event4.eventClimax
    def event5():
        import event5
        return event5.eventClimax
    def event6():
        import event6
        return event6.eventClimax
    def eventCli1():
        import eventCli1
        return eventCli1.eventClimax
    def eventCli2():
        import eventCli2
        return eventCli2.eventClimax
    def goodEnd():
        import goodEnd
        return goodEnd.eventClimax
    def badEnd():
        import badEnd
        return badEnd.eventClimax
    #when you are done you destroy the object and we will just remake it later when we re need it so that we don't have code loaded that is now useless since the event passed already
    def __del__(self):
        print("destroyed")
