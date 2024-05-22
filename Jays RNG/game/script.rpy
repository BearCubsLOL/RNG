python:
    import random
    import json


define e = Character("Eileen")


label start:
    python:
        with open("all_saves.txt") as f:
            data = json.load(f)

        def check_inventory():
            if data["coins"] == 50:
                renpy.jump.idk
    $ check_inventory()
    jump inventory
    
label inventory:
    "idk rn"

label idk:
    "dude"