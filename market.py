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
    username = "Pedro"
    return render_template("about.html",current_user=username)

## dynamic routes, taking a varaible and using it as a route
## need the <varibale_name> format int the route section
@app.route("/about/<username>")
def about_user_page(username):
    ## needs to be a formatted print statement
    username = "Pedro" 
    return f'<h1>This is now the baout page of whatever is put in the url page, basically up to the user {username}</h1>'

##home page for the application
## need render_tempplates function from flask package, need a astring argument
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/Products")
def products_page():
    return render_template("products.html", product="Door handle")
