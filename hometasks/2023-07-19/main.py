import os
import sqlite3

from flask import Flask, render_template, request, abort, redirect, flash, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

from database import DataBase, User

from config import *

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(__name__)
app.config.update({'DATABASE': os.path.join(app.root_path, 'flask.db')})

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('create_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


@login_manager.user_loader
def load_user(user_id):
    db_con = connect_db()
    dbase = DataBase(db_con)
    user_data = dbase.get_user(user_id)
    # db_con.close()

    if user_data:
        return User(user_id)
    return None


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    db_con = connect_db()
    dbase = DataBase(db_con)
    user_data = dbase.get_user_by_username(username)

    if user_data and user_data['password'] == password:
        user_id = user_data['id']
        user = User(user_id)
        login_user(user)

        session['username'] = user_data['username']
    else:
        flash('Invalid credentials. Please try again.', 'error')
    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    dbase = DataBase(db_con)

    username = session.get('username', None)
    return render_template('index.html', title='Home', menu=dbase.get_objects('navbar'),
                           posts=dbase.get_objects('posts'), username=username)


@app.route('/post/<post_id>')
def show_post(post_id):
    db_con = connect_db()
    dbase = DataBase(db_con)

    post = dbase.get_post(post_id)
    if not post:
        abort(404)

    comments = dbase.get_comments(post_id)
    username = session.get('username', None)

    return render_template('post.html', post=post, comments=comments, title=post['title'],
                           menu=dbase.get_objects('navbar'), username=username, comment_owner=dbase.get_user)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def add_comment(post_id):
    db_con = connect_db()
    dbase = DataBase(db_con)
    username = session.get('username', None)
    post = dbase.get_post(post_id)
    if not post:
        abort(404)

    if request.method == 'POST' and "<div>" not in request.form['text'] and len(request.form['text']) > 0:
        res = dbase.add_comment(request.form['text'], post_id, username)
        if res:
            print('Comment added successfully')
        else:
            print('Failed to add comment')

    return redirect(f'/post/{post_id}')


@app.route('/about')
def about():
    db_con = connect_db()
    dbase = DataBase(db_con)
    username = session.get('username', None)
    return render_template('about.html', title='About', menu=dbase.get_objects('navbar'), username=username)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    db_con = connect_db()
    dbase = DataBase(db_con)
    username = session.get('username', None)
    show_thank_you = session.pop('show_thank_you', False)

    if request.method == 'POST':
        res = dbase.send_feedback(request.form['name'], request.form['email'], request.form['message'])
        if res:
            print('Feedback sent successfully')
        else:
            print('Failed to send feedback')

        session['show_thank_you'] = True
        return redirect('/contact')

    return render_template('feedback_form.html', title='Contact Us', menu=dbase.get_objects('navbar'),
                           username=username, show_thank_you=show_thank_you)


@app.errorhandler(404)
def page_not_found(error):
    db_con = connect_db()
    dbase = DataBase(db_con)
    username = session.get('username', None)
    return render_template('page404.html', title='Page Not Found', menu=dbase.get_objects('navbar'), username=username)


if __name__ == '__main__':
    create_db()
    app.run()
