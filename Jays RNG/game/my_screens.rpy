
image best_hover = "thebest_hover.png"

label myScreens:

screen mapScreen:
    add "black"

    imagebutton:
        xpos 1750
        ypos 360
        idle "inventory_button_idle"
        hover "inventory_button_hover"
        action Jump("inventory")