class Movie():
    """
    This class will store all movie related data returned by API in instance
    variables.
    Instance variables: title, storyline, poster_image_url, trailer_youtube_url
    """
    def __init__(
                 self, movie_title, movie_storyline, movie_poster_url,
                 movie_trailer_url):
        #   initialising all instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
