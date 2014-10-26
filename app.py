# --- Flask Hello World --- #

#import the Flask class from the flask module

from flask import Flask

#create app object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# definte the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# start dev server using run() method

if __name__ == "__main__":
	app.run()