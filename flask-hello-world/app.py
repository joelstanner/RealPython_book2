# - flask hello world

# import flask class from flask module
from flask import Flask

#create the application object
app = Flask(__name__)
app.config["DEBUG"] = True

# use decorators to link the function to a URL
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello World!?!?!?!?!!?!?"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# start the development server using the run() method
if __name__ == '__main__':
    app.run()


