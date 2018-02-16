import webbrowser


class Movie():
    """This class is used to store movie related information"""
    # Function gets title,story,image and trailer

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Class inheritance from movies.


class TV_Show_Movies(Movie):
    """This class is used to store TV show movies and related info."""
    # Function gets title,story,image and trailer
    def __init(self, tv_title, tv_storyline, poster_image, trailer_youtube):
        # Inherits poster_image and trailer_youtube
        Movie.__init__(poster_image, trailer_yotube)
        self.tv_title = tv_title
        self.tv_storyline = tv_storyline
