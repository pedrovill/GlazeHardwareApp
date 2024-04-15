from flask import Flask, render_template

## __name__ is a variable built into python to refer to the file youre working on.
app = Flask(__name__)

## decoratrors go before function
## .route tell what url the function wiill be routing to
## @app.route("/")
##  def hello_world():
##   return '<h1>New changes to the website son again</h1>'

@app.route("/about")
def about_page():
    return '<h1>This is the about page</h1>'

## dynamic routes, taking a varaible and using it as a route
## need the <varibale_name> format int the route section
@app.route("/about/<username>")
def about_user_page(username):
    ## needs to be a formatted print statement 
    return f'<h1>This is now the baout page of whatever is put in the url page, basically up to the user {username}</h1>'

##home page for the application
## need render_tempplates function from flask package, need a astring argument
@app.route("/")
def home_page():
    return render_template("home.html")