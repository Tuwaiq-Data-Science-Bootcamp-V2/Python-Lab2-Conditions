"""
This code is created to recommend a movie for a friend
The recommendation is based in movie rating and movie popularity... 
"""

# Create the required variables
movie_name = "Avatar"
movie_rate = 3
movie_popularity = 72.65

"""
If condition that will show the result of the recommendation based
in the rating and popularity 
"""


if movie_rate >= 4 and movie_popularity > 80:
    print("\nHighly recommended\n")
elif movie_rate >= 3 and movie_popularity > 70:
    print("\nI recommended it, It is good\n")
elif movie_rate <= 2 and movie_popularity > 60:
    print("\nYou should check it out!\n")
else:
    print("\nDon't watch it, It is a waste of time\n")


"""
************* ANOTHER WAY TO SOLVE *************

if movie_rate >= 4 and movie_popularity > 80:
    print("\nHighly recommended\n")
elif movie_rate >= 3 and movie_popularity > 70:
    print("\nI recommended it, It is good\n")
elif movie_rate <= 2 and movie_popularity > 60:
    print("\nYou should check it out!\n")
elif movie_rate <= 2 and movie_popularity < 50:
    print("\nDon't watch it, It is a waste of time\n")

************************************************
"""