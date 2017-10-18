import media
import fresh_tomatoes
import requests

# API key for authentication
API_KEY = "f0cbe4c6016caabd60d267c20059dda5"
# urls for making api calls to get movie details
POPULAR_MOVIES_URL = ("http://api.themoviedb.org/3/discover/movie?"
                      "%20%E2%86%B5sort_by=popularity.desc?&api_key={key}")
VIDEOS_URL = "https://api.themoviedb.org/3/movie/{id}/videos?api_key={key}"
MOVIE_POSTER_BASE_URL = "http://image.tmdb.org/t/p/original"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="


# Returns an array of objects containing popular movies details in json format
def get_popular_movies():
    url = POPULAR_MOVIES_URL.format(key=API_KEY)
    result = requests.get(url).json()
    return result["results"]


# Returns an video code containing particular movie id
def get_video_key(id):
    url = VIDEOS_URL.format(id=id, key=API_KEY)
    result = requests.get(url).json()
    return result["results"][0]["key"]


# returns a list of class Movie objects
def get_movies_object_list():
    movies = []
    popular_movies = get_popular_movies()

    for i in range(0, len(popular_movies)):
        id = popular_movies[i]["id"]
        movie_title = popular_movies[i]["title"]
        movie_storyline = popular_movies[i]["overview"]
        movie_poster_url = (MOVIE_POSTER_BASE_URL +
                            popular_movies[i]["poster_path"])
        trailer_source = get_video_key(id)
        movie_youtube_trailer = YOUTUBE_BASE_URL + trailer_source
        # initialising class Movie
        movie_object = media.Movie(movie_title, movie_storyline,
                                   movie_poster_url, movie_youtube_trailer)
        movies.append(movie_object)
    return movies

movies = get_movies_object_list()
fresh_tomatoes.open_movies_page(movies)
