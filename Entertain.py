import fresh_tomatoes
import movie
# Use import to bring properties of fresh_tomatoes
# and movie to this python file.

# Instances of Class ... Types of movies
toy_story = movie.Media(
            "Toy story",
            "A story of a boy and his toys coming to life",
            "http://www.crankycritic.com/archive/posters/toystory.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Class variables invoking the class Media. using the name of the files
# + '.' + name of class eg movie.Media()
# Class should always be in Capital letters

Avengers = movie.Media(
            "Avengers",
            "A story of a group of superhumans trying to save earth",
            "http://cdn.collider.com/wp-content/uploads/avengers-movie-poster-1.jpg",  # NOQA
            "https://www.youtube.com/watch?v=tmeOjFno6Do")


Planet_of_apes = movie.Media(
                'Planet of Apes',
                "A story of apes that can fight",
                'https://fanart.tv/fanart/movies/119450/movieposter/dawn-of-the-planet-of-the-apes-5472b7b6bca05.jpg',  # NOQA
                'https://www.youtube.com/watch?v=3sHMCRaS3ao')

Spiderman = movie.Media(
            'Spiderman',
            "A story of a boy and his"
            "super powers after being bit by a spider",
            'https://pics.filmaffinity.com/spider_man_homecoming-336093112-large.jpg',  # NOQA
            'https://www.youtube.com/watch?v=39udgGPyYMg')

Kingsman = movie.Media(
            'Kingsman S.S',
            "A story of a man and his elite fighting techniques",
            'https://i.pinimg.com/originals/45/df/6a/45df6a4bb96e76827bdaaf2897d77212.jpg',  # NOQA
            'https://www.youtube.com/watch?v=kl8F-8tR8to')

Black_Panther = movie.Media(
                "Black Panther",
                "A story of a rich black man and his fancy toys",
                'http://i.dailymail.co.uk/i/pix/2017/06/10/19/4148FD2800000578-4591774-Revealed_Marvel_released_teaser_poster_for_Black_Panther_on_Frid-m-107_1497118337020.jpg',  # NOQA
                'https://www.youtube.com/watch?v=dxWvtMOGAhw')


movies = [
    toy_story, Avengers, Planet_of_apes, Spiderman, Kingsman, Black_Panther]
fresh_tomatoes.open_movies_page(movies)
# Movies is a list passed into the function '.open_movies_page'
# Remember to always use the name of the file followed by the function eg
# 'fresh_tomatoes' followed by '.' then open_movies_page()