#Every time a event gets succes or failed then its added into this dictionary so it can easely be accesed later in the game when we need to call them
eventSucces = { "kanndyEvent1": True , "kanndyevent2": False }
#the dic works like this the key is the name of the of the character + the event and the value if it succesed or not
import eventHandler

student = eventHandler.Student("kanndy")
event = student.event1()
eventSucces['eventTest'] = event
del student
print(eventSucces['eventTest'])
