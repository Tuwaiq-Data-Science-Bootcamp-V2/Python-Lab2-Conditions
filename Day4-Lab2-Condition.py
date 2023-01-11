# Create a variable for a movie.
fav_movie = 'The Godfather'

# My rating of the movie out of 5
rate = 3

# Popularity score of the movie
score = 72.65

''' Check if the movie rating is 4 or greater and the popularity is greater
than 80, print "Highly recommended".
Else if the movie rating is 3 or greater and the popularity is greater than 70,
print "I recommended it, It is good".
Else if the movie rating is 2 or less and the popularity is greater than 60,
print "You should check it out!".
Else the movie rating is 2 or less and the popularity is less than 50, print
"Don't watch it, It is a waste of time"..'''

if rate >= 4 and score > 80:
    print ('Highly recommended')
elif rate < 4 and rate > 3 and score <= 80 and score > 70:
    print ('I recommended it, It is good')
elif rate <= 3 and rate >= 2 and score <= 70 and score > 60:
    print ('You should check it out\!')
else:
    print ('Don\'t watch it, It is a waste of time')
