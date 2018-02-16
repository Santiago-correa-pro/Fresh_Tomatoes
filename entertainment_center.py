import fresh_tomatoes
import media
import requests


# Movie title , Movie Story , Movie box cover and Movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://i.imgur.com/TpMrf4M.jpg",
    "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://www.halon.com/wp-content/uploads/2010/07/avatar_poster1.jpg",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")
insidious = media.Movie(
    "Insidious: The Last Key",
    " A parapsychologist continues her voyage into the further",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTE0r-ZiGH8aV-Nz4j9KHtrv_UdL-rioSlcb8PGkUHjxaoUxolc",
    "https://www.youtube.com/watch?v=pXJC4mZmU_U")
friends = media.TV_Show_Movies(
    "Friends",
    "A group of friends learning how to live together",
    "https://vignette.wikia.nocookie.net/friends/images/2/20/P183931_b_v8_ac.jpg/revision/latest?cb=20160929100417",
    "https://www.youtube.com/watch?v=Gpa5S8DgPzs")

# Using TheMovieDb api to get title of movies
req_blade_runner = requests.get(
    "https://api.themoviedb.org/3/movie/335984?api_key=426751a9d48233ac9475b48847c77d13")

# Get results in JSON format
blade_runner_data = req_blade_runner.json()

blade_runner = media.Movie(
    blade_runner_data[u'original_title'],
    "K's discovery leads him on a quest to find Rick Deckard",
    "https://media1.fdncms.com/portmerc/imager/u/original/19361423/158974_af.jpg",
    "https://www.youtube.com/watch?v=6T2b0mp2hco")

req_fight_club = requests.get(
    "https://api.themoviedb.org/3/movie/550?api_key=426751a9d48233ac9475b48847c77d13")

fight_club_data = req_fight_club.json()

fight_club = media.Movie(
    fight_club_data["original_title"],
    "Their concept catch on with underground fight clubs.",
    "https://timedotcom.files.wordpress.com/2014/07/poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")


# Array of Movies is created since the open_movies_page function accepts
# an array
movies = [toy_story, avatar, insidious, friends, fight_club, blade_runner]
fresh_tomatoes.open_movies_page(movies)
