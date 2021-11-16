import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results


#Here’s an executable sample, using the optional params parameter of requests.get
import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched


#You would want to contact the datamuse API repeatedly, passing different values associated with the key rel_rhy
# import statements for necessary Python modules
import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))


#GRADED EXAM

#EXERCISE1 

import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
def get_movies_from_tastedive(film):
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction['q'] = film
    params_diction['type'] = 'movies'
    params_diction['limit'] = 5
    taste=requests_with_caching.get('https://tastedive.com/api/similar', params=params_diction)
    return json.loads(taste.text) #or taste.json()
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_movies_from_tastedive("Bridesmaids"))
print(get_movies_from_tastedive("Black Panther"))

#EXERCISE2

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
def get_movies_from_tastedive(film):
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction['q'] = film
    params_diction['type'] = 'movies'
    params_diction['limit'] = 5
    taste=requests_with_caching.get('https://tastedive.com/api/similar', params=params_diction)
    return taste.json()
def extract_movie_titles(film):
    return [d['Name'] for d in film['Similar']['Results']]
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(extract_movie_titles(get_movies_from_tastedive("Tony Bennett")))
print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))



#EXERCISE3

def get_related_titles(titles_list):
    list = []
    for i in titles_list:
        new_list = extract_movie_titles(get_movies_from_tastedive(i))
        for i in new_list:
            if i not in list:
                list.append(i)
    print(list)
    return list


#EXERCISE4

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))


#EXERCISE5

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 


#EXERCISE6

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]