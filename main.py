############## Minimal App#########
from flask import Flask, url_for

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1><p>Hello, World in paragraph!</p>"+name

# flask --app hello run
# flask --app hello run --debug : to enable debug mode
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

########## HTML Escaping ##############
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

####### Routing ##########
# Use the route() decorator to bind a function to a URL.


##############   Viariable Rules ##################
# <converter:variable_name>
#  string,
#  int,
#  float,
#  path(accepts slashes),
#  uuid (accepts UUID strings)

##############  Unique URLs / Redirection Behavior ##################
@app.route('/projects/') #trailing slash
def projects():
    return 'The project page' 

@app.route('/about')
def about():
    return 'The about page' #/about/ ==> 404error

################ HTTP METHODS ################
from flask import request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
def do_the_login():
    return "do_the_login"
def show_the_login_form():
    return "show_the_login"

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

#################  Static Files  ########################
# url_for('static', filename='style.css')

###############  Accessing Request Data #################


###############  Redirects and Errors #################
from flask import abort, redirect, url_for

@app.route('/red')
def red():
    return redirect(url_for('other'))

@app.route('/other')
def other():
    return "redirected with success"

@app.route('/err')
def err():
    return redirect(url_for('error_page'))

@app.route('/error_page')
def error_page():
    abort(401)
print(__name__ )
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)