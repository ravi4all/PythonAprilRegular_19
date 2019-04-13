# Sets

dataset = {
    "action" : ['kgf','thor','hulk','ironman','superman','batman','avengers',
                'baahubali','antman','mi','nfs','lucy','race','sultan'],
    "comedy" : ['dhamaal','antman'],
    "drama" : ["kgf","lucy","race","baahubali"]
    }

user_1 = {'kgf','thor','hulk','ironman','superman','batman','avengers','baahubali','antman','dhamaal'}
user_2 = {'thor','ironman','avengers','baahubali','mi','nfs','lucy','race','sultan','dhamaal'}

#JaccardDistance - len(intersection) / len(union)
j = len(user_1.intersection(user_2)) / len(user_1.union(user_2))
sim = 1 - j
print("Similarity b/w 2 users",round(sim*100,2))
'''
1. Find the number of movies according to the categories they have watched
2. Recommend movies to user_2 which user_2 has not watched but user_1 has
watched and it must belongs to the category where they have most number of common
category movies
'''
print("Similar movies are",user_1.intersection(user_2))
simMovies = user_1.intersection(user_2)
action = 0
comedy = 0
drama = 0

for movie in simMovies:
    if movie in dataset["action"]:
        action = action + 1
    elif movie in dataset["comedy"]:
        comedy += 1
    elif movie in dataset['drama']:
        drama += 1
print(f"Action : {action}, Drama : {drama}, Comedy : {comedy}")

m = []

for movie in user_1:
    if movie in dataset["action"]:
        #print(movie)
        m.append(movie)
'''
for movie in dataset["action"]:
    if movie not in user_2:
        print("Recommended :",movie)
'''

for movie in m:
    if movie not in user_2:
        print("Recommended :",movie)
