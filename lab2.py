movie_name="Run"
movie_rate = 3
movie_popularity=72.65

if movie_rate >= 4 and movie_popularity > 80:
    print("Highly recommended")
elif movie_rate >= 3 and movie_popularity > 70:
    print("I recommended it, It is good")
elif movie_rate <= 2 and movie_popularity > 60:
    print("You should check it out!")
elif movie_rate <= 2 and movie_popularity > 50:
    print("Don't watch it, It is a waste of time")
