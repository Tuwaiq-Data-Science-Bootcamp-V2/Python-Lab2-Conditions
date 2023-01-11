#!/usr/bin/env python
# coding: utf-8

# In[10]:


best_movie =  'Smile'
mov_rate = 3
popularity_score = 72.65


# In[11]:


if mov_rate >= 4 and popularity_score > 80:
    print('Highly recommended')
elif mov_rate >=3 and popularity_score > 70:
    print('I recommended it, It is good')
elif mov_rate <=2 and popularity_score > 60:
    print( "You should check it out!")
elif  mov_rate <=2 and popularity_score < 50:
    print ("Don't watch it, It is a waste of time")


# In[ ]:




