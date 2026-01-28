# The following simple dictionary stores information about one specific alien
# The alien_0 dictionary stores two attributes: color and points. The following two print commands read this information from the dictionary and display it on the screen:
alien_0 = {"colour": "Green", "points": 5}

print(alien_0 ["colour"])
print(alien_0 ["points"])
#
alien_0 = {"colour": "green", "points": 5}

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
#
alien_0 = {"colour": "green", "points": 5}
print(alien_0)

alien_0["x-position"] = 0
alien_0["y-position"] = 25
print(alien_0)
