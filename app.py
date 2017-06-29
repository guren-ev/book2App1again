#----- Flask Hello World -----#  

from flask import Flask

# create the application object

app = Flask(__name__)

# error handeling
app.config["DEBUG"] = True

# use the decorator pattern to
# to link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "!!!!!!!!!!!!!!!!!!!!!!!!!1Hello, World!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#RESPONSIVE OBJECTS
@app.route("/name/<name>")
def index(name):
    if name.lower() == "welebi":
        return "Hello {}".format(name)
    else:
        return "Not Found", 404



# start the develpmetn server using the run() method
if __name__ == "__main__":
    app.run()

