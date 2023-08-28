"""
This function recommends movies
based on ratings from a user.
The function accepts a dictionary 
in the form :
{
    "movie1"=<value>,
    "movie2"=<value>, 
...
}
"""
import random
movie_database = [f'movie_{i}' for i in range(1, 1000)]
random.shuffle(movie_database)
def recommend_movies(user_input):
    """
    Do something here with user input
    """
    ...
    return movie_database[:3]

if __name__ == "__main__":
    user_input = {"movie1":3, "movie3": 2, "movie50": 4}
    movies = recommend_movies(user_input=user_input)
    print(movies)
