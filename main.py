# builtin
import glob
# external
import flask
# local
from lib import utils


# start app and set configuration
app = flask.Flask(__name__, static_folder='static', static_url_path='/static', )
utils.setup(app)


# Views! i.e. what the user gets when they type in our url

# this renders the readme as the index page...
@app.route('/')
def index ():
    return flask.render_template('partials/base.html',
        content=utils.read_file("readme.md"))

# ...but this is the index page view you probably want
# @app.route('/')
# def index ():
#     return flask.render_template('index.html')

@app.route('/example')
def example_route():
    return flask.render_template('partials/base.html',
        content='''
# Example Page

You can create an entire new page be adding content inline here!

You probably shouldn't, but you can.

Syntax is markdown, and the lack of column alignment is on purpose
    ''')

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('partials/base.html',
        content='# Error 404\nPage not found'), 404

@app.errorhandler(500)
def server_error(e):
    return flask.render_template('partials/base.html',
        content='# Error 500\nServer error'), 500


if __name__ == '__main__':
    app.run(port = app.config.get("PORT", 5000))
