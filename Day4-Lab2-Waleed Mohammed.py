
movie = 'One Piece'
RatMovie = 3
PopularityScore = 72.65

if RatMovie >= 4 and PopularityScore > 80:
	print('Highly recommended')

elif RatMovie >= 3 and PopularityScore > 70:
	print('I recommended it, It is good')

elif RatMovie <= 2 and PopularityScore > 60:
	print('You should check it out!')

elif RatMovie <= 2 and PopularityScore < 50:
	print("Don't watch it, It is a waste of time")