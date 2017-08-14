# This creates the class media
class Media():
    # Using def __init__ () initializes the class
    # Parameters are inserted into the class eg movie_title.
    # Always remember to use 'self' first.
    def __init__(
        self, movie_title, movie_storyline, poster_image, trailer_youtube):
    	self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube