#Every time a event gets success or failed then its added into this dictionary so it can easily be accessed later in the game when we need to call them
eventSuccess = { "kanndyEvent1": True , "kanndyevent2": False }
#the dict works like this the key is the name of the of the character + the event and True/False whether it succeeded or not
import eventHandler

student = eventHandler.Student("kanndy")
event = student.callEvent(1)
eventSuccess['eventTest'] = event
del student
student2 = eventHandler.Student("lily")
event2 = student2.callEvent(2)
eventSuccess["eventTest2"] = event2
del student2
print(eventSuccess['eventTest'])
