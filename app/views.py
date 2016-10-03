from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Greetings World! It is I, the marvelous masticator!  Watch as I chew some stuff!'

@app.route('/bingo')
def bingo():
    return 'Bing time!!!'
