init python:
    import random
    import all_saves


define e = Character("Eileen")
define idk = Character("Hi")


label start:
    $ for_now = "Health:" + str(all_saves.data["Health"])
    
    idk "[for_now]"

    $ all_saves.data["Health"] += 50

    $ for_now = "Health:" + str(all_saves.data["Health"])
    
    idk "[for_now]"

    jump inventory
    
label inventory:
    "idk rn"

label idk:
    "dude"