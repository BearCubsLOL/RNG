python:
    inventory = all_saves.data["inventory"]

    def detectInventoryItem(key, number):
        if inventory[key] == "ManaPot":
            item[number] = "ManaPot.png"

label inventory:
    "idk rn"

    python:
        times = 1
        for items in inventory:
            times += 1
            detectInventoryItem(0)
    

    return