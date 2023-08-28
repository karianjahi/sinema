from flask import Flask

# Let us tell flask that this is the script that launches the project
app = Flask(__name__)

# Create a function that says hello world on the browser
# The function must container a decorator that specifies the url on which to launch the output
@app.route("/")
def hello_world():
    return "<h1>hello world</h1>"

# Create a new function that recommends movies to a user
# The path (url) shall be "/recommender"
@app.route("/recommender")
def recommend_movies():
    some_movies = ["movie1", "movie2", "movie3"]
    return f'''<title>recommendations</title>
                <h1>The following movies are recommended</h1>
                <ol>
                    <li>{some_movies[0]}</li>
                    <li>{some_movies[1]}</li>
                    <li>{some_movies[2]}</li>
                </ol>
            '''

# We can start our server locally.
# To make sure the server is launched only when this script
# is run directly (and not through another script):
if __name__ == "__main__":
    app.run(debug=True, port=5000)

