if time <= 0 or fuel <= 0 or (hit_wall == True and extra_life == False) or \
    (hit_obstacle == True and extra_life == False):
    print("You died.")
elif hit_wall == true and extra_life == True:
    extra_life == False
else:
    print("You can proceed to the next level!")
