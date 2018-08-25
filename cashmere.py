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
    return render_template('index.html')

@app.route('/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/productions/')
def productions():
    articles = get_articles("productions")
    print(articles)
    return render_template('productions/index.html', pages=articles)

@app.route('/productions/<path:path>/')
def production_article(path):
    page = flatpages.get_or_404(path)
    return render_template('productions/page.html', page=page)

@app.route('/pipeline/')
def pipeline():
    articles = get_articles("pipeline")
    return render_template('pipeline/index.html', pages=articles)

@app.route('/pipeline/<path:path>/')
def pipeline_article(path):
    page = flatpages.get_or_404(path)
    return render_template('pipeline/page.html', page=page)

@app.route('/services/')
def services():
    articles = get_articles("services")
    return render_template('services/index.html', pages=articles)

@app.route('/services/<path:path>/')
def services_article(path):
    page = flatpages.get_or_404(path)
    return render_template('services/page.html', page=page)

@app.route('/courses/')
def courses():
    articles = get_articles("courses")
    return render_template('courses/index.html', pages=articles)

@app.route('/courses/<path:path>/')
def courses_article(path):
    page = flatpages.get_or_404(path)
    return render_template('courses/page.html', page=page)

@app.route('/demos/')
def demos():
    articles = get_articles("demos")
    return render_template('demos/index.html', pages=articles)

@app.route('/demos/<path:path>/')
def demos_article(path):
    page = flatpages.get_or_404(path)
    return render_template('demos/page.html', page=page)

# @app.route('/about/')
# def about():
#     page = flatpages.get_or_404("about.html")
#     return render_template('about.html', page=page)


# === get articles === #

def get_articles(path_name, reverse=False):
    """ Returns all published blog articles ordered by date. """
    articles = [p for p in flatpages if p.path.startswith(path_name)]
    # articles = [p for p in articles if p.meta.get('published', False)]
    articles = sorted(articles,
                      reverse=reverse,
                      key=lambda k: k.meta['date'])
    return articles

if __name__ == "__main__":
    app.run(debug=True)
