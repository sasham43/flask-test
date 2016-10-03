from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', form=form, title='Sign In',providers=app.config['OPENID_PROVIDERS'])
