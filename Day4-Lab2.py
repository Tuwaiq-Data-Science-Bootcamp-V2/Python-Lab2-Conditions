#movie name
movie_name = "Green Book"

#movie's rate
movie_rate = 3

#movie popularity 
movie_popularity = 72.65

#dictionary for movie
movie = {"name":movie_name, "rate":movie_rate, "popularity":movie_popularity}

#if statement to check if the movie has a great rating and popularity or not, and print a message depending on the values
if movie["rate"] >= 4 and movie["popularity"] >= 80:
    print("Highly recommended")
elif movie["rate"]>=3 and movie["popularity"] >= 70:
    print("I recommended it, It is good") 
elif movie["rate"]<=2 and movie["popularity"] >= 60:
    print("You should check it out!")
elif movie["rate"]<=2 and movie["popularity"] < 50:
    print("Don't watch it, It is a waste of time")