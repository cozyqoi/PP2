movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
#task 1
def is_high_imdb(movie):
    return movie["imdb"] > 5.5

film_name = input("atyn engiziniz: ")
found_movie = None
for m in movies:
    if m["name"].lower() == film_name.lower():
        found_movie = m
        break 

if found_movie:
    print("reiting > 5.5? " + str(is_high_imdb(found_movie)))
else:
    print("film jok.")

#task 2
def high_imdb_movies(movies_list):
    result = []
    for m in movies_list:
        if m["imdb"] > 5.5:
            result.append(m)
    return result

print("reiting > 5.5:")
for movie in high_imdb_movies(movies):
    print("- " + movie["name"] + " (IMDB: " + str(movie["imdb"]) + ")")

#task 3
def movies_by_category(movies, category):
    result = []
    for m in movies:
        if m["category"].lower() == category.lower():
            result.append(m)
    return result

category = input("category engiziniz: ")
result = movies_by_category(category)

if result:
    print("category films '" + category + "':")
    for movie in result:
        print("- " + movie["name"])
else:
    print("category tabylmady.")    

#task 4
def average_imdb(movies_list):
    total = 0
    for m in movies_list:
        total += m["imdb"]
    return total / len(movies_list)


average = average_imdb(movies)
print("average: {:.1f}".format(average))

#task 5
def category_average_imdb(category):
    category_movies = movies_by_category(category)
    if not category_movies:
        return 0
    
    total = 0
    for m in category_movies:
        total += m["imdb"]
    
    return total / len(category_movies)


category = input("category engiziniz: ")
average = category_average_imdb(category)

if average == 0:
    print("category tabylmady.")
else:
    print("AVG '{}': {:.1f}".format(category, average))
