from flask import Flask, render_template

app = Flask(__name__)

menu = [{'name': 'Home', 'url': 'index'},
        {'name': 'About', 'url': 'about'},
        {'name': 'Contact Us', 'url': 'contact'}
        ]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Home', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='About', menu=menu)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us', menu=menu)


if __name__ == '__main__':
    app.run()
