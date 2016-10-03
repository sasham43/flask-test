from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'Rodrigo'},
            'body': 'Once I ate a clam, but it was not good.  Then I ate a cheese, and it was good.'
        },
        {
            'author': {'nickname': 'Donnarumma'},
            'body': 'Legends tell of a portly masseuse named Gene who will one day rule the world.'
        }
    ]
    return render_template('index.html', subtitle='A City for Flasks', user=user, posts=posts)
