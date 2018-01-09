#!venv/bin/python

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_bootstrap import Bootstrap


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

def create_bootstrap_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

app = create_bootstrap_app()
app.config.from_object(__name__)
flatpages = FlatPages(app)

@app.route('/')
def index():
    pages = (p for p in flatpages if 'date' in p.meta)
    return render_template('index.html', pages=pages)

@app.route('/pages/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/pipeline/<path:path>')
def pipeline():
    page = flask_flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/about')
def about():
    pages = (p for p in flatpages if 'date' in p.meta)
    return render_template('about.html', pages=pages)



if __name__=="__main__":
    app.run(debug=True)

