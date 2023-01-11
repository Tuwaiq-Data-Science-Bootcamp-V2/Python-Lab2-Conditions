movie = " Sonic the movie"
movieRate = 3
popularityScore =  72.65
if movieRate >= 4 :
    if popularityScore > 80:
        print("Highly recommended")
elif movieRate >= 3:
    if popularityScore > 70:
        print("I recommended it, It is good")
elif movieRate <= 2:
    if popularityScore > 60:
        print("You should check it out!")
elif movieRate <= 2:
    if popularityScore < 50:
        print("Don't watch it, It is a waste of time")
        