# OMDB and TasteDive

import requests
import json

# get a dictionary from tastedrive api with the recomended movies related with the selected movie 
def get_movies_from_tastedive(str_td):
    base_url = 'https://tastedive.com/api/similar'
    parameters = {}
    parameters['q'] = str_td
    parameters['type'] = 'movies'
    parameters['limit'] = 5
    page_td = requests.get(base_url, params=parameters)
    #page_td_url = page_td.url
    #print(page_td_url)
    data_td = page_td.json()
    #print(data_td)
    return(data_td)

# get a list of the recomended movies related with a selected movie
def extract_movie_titles(str_td):
    dic_td = get_movies_from_tastedive(str_td)
    #print(dic_td)
    #json_dic_td = json.dumps(dic_td, indent=2)
    #print(json_dic_td)
    movies = []
    for movie in dic_td['Similar']['Results']:
        movies.append(movie['Name'])
    #print(movies)
    return movies

# get a list of the recomended movies related from a list of movies:
def get_related_titles(lst_movies):
    all_movies = []
    for movie in lst_movies:
        n_lst = extract_movie_titles(movie)
        for item in n_lst:
            if item not in all_movies:
                all_movies.append(item)
    #print(all_movies)
    return all_movies

# get a dictionary from omdb api with the information of the ranking of the selected movie 
def get_movie_data(movie_name):
    base_url = 'http://www.omdbapi.com/'
    parameters = {}
    parameters['t'] = movie_name
    parameters['r'] = 'json'
    parameters['apikey']='1f63b963'
    page_omdb = requests.get(base_url, params=parameters)
    #page_omdb_url = page_omdb.url
    #print(page_omdb_url)
    data_omdb = page_omdb.json()
    return data_omdb

# get a "Rotten Tomatoes" ranking of a selected movie
def get_movie_rating(movie_name):
    dic_omdb = get_movie_data(movie_name)
    #print(dic_omdb)
    #json_dic_td = json.dumps(dic_omdb, indent=2)
    #print(json_dic_td)
    rotten_tomatoes = 0
    for dic in dic_omdb['Ratings']:
        if dic['Source'] == 'Rotten Tomatoes':
            rotten_tomatoes = int(dic['Value'][:dic['Value'].find('%')])
    return(rotten_tomatoes)

# get a list of recomended movies sorted by "Rotten Tomatoes" ranking
def get_sorted_recommendations(lst_movies):
    final_recommended = sorted(get_related_titles(lst_movies), key=lambda movie: (get_movie_rating(movie), movie), reverse=True)
    return final_recommended

# user interantion
movies = []
while True:
    movie = input('What movie do you like to look for related movies (press just "Enter" to finish): ')
    if len(movie) > 0: 
        movies.append(movie)
    else:
        print(movies)
        break

print(get_sorted_recommendations(movies))
