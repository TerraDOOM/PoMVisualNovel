#Every time a event gets success or failed then its added into this dictionary so it can easily be accessed later in the game when we need to call them
eventSuccess = { "kanndyEvent1": True , "kanndyevent2": False }
#the dict works like this the key is the name of the of the character + the event and True/False whether it succeeded or not
import eventHandler

student = eventHandler.Student("kanndy")
event = student.event1()
eventSuccess['eventTest'] = event
del student
print(eventSuccess['eventTest'])
