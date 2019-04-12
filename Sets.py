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
