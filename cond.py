movie='top gun'
rating=3
pop_score=72.65

if rating >= 4 and pop_score > 80 :
    print('Highly recommended')
elif rating >=3 and pop_score > 70:
    print("I recommended it, It is good")
elif rating <= 2 and pop_score> 60:
    print("You should check it out!")
elif rating <= 2 and pop_score < 50:
    print("Don't watch it, It is a waste of time")