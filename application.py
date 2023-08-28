from flask import Flask

# Let us tell flask that this is the script that launches the project
app = Flask(__name__)

# Create a function that says hello world on the browser
# The function must container a decorator that specifies the url on which to launch the output
@app.route("/")
def hello_world():
    return "hello world"

# We can start our server locally.
# To make sure the server is launched only when this script
# is run directly (and not through another script):
if __name__ == "__main__":
    app.run(debug=True, port=5000)

