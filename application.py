from flask import Flask, render_template
from simple_recommender import recommend_movies

# Let us tell flask that this is the script that launches the project
app = Flask(__name__)

# Create a function that says hello world on the browser
# The function must container a decorator that specifies the url on which to launch the output
@app.route("/")
def index():
    return render_template("index.html")

# Create a new function that recommends movies to a user
# The path (url) shall be "/recommender"
@app.route("/recommender")
def recommendations():
    user_input = ""
    movies = recommend_movies(user_input)
    return render_template("recommendations.html", movies=movies)

# We can start our server locally.
# To make sure the server is launched only when this script
# is run directly (and not through another script):
if __name__ == "__main__":
    app.run(debug=True, port=5000)

