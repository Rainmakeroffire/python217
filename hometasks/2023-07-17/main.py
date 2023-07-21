import os
import sqlite3

from flask import Flask, render_template, request, abort, redirect

from database import DataBase

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(__name__)
app.config.update({'DATABASE': os.path.join(app.root_path, 'flask.db')})


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


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    dbase = DataBase(db_con)
    return render_template('index.html', title='Home', menu=dbase.get_objects('navbar'),
                           posts=dbase.get_objects('posts'))


@app.route('/post/<post_id>')
def show_post(post_id):
    db_con = connect_db()
    dbase = DataBase(db_con)

    post = dbase.get_post(post_id)
    if not post:
        abort(404)

    comments = dbase.get_comments(post_id)

    return render_template('post.html', post=post, comments=comments, title=post['title'], menu=dbase.get_objects('navbar'))


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def add_comment(post_id):
    db_con = connect_db()
    dbase = DataBase(db_con)

    post = dbase.get_post(post_id)
    if not post:
        abort(404)

    if request.method == 'POST':
        res = dbase.add_comment(request.form['text'], post_id)
        if res:
            print('Comment added successfully')
        else:
            print('Failed to add comment')

    return redirect(f'/post/{post_id}')


@app.route('/about')
def about():
    db_con = connect_db()
    dbase = DataBase(db_con)
    return render_template('about.html', title='About', menu=dbase.get_objects('navbar'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    db_con = connect_db()
    dbase = DataBase(db_con)
    return render_template('contact.html', title='Contact Us', menu=dbase.get_objects('navbar'))


@app.errorhandler(404)
def page_not_found(error):
    db_con = connect_db()
    dbase = DataBase(db_con)
    return render_template('page404.html', title='Page Not Found', menu=dbase.get_objects('navbar'))


if __name__ == '__main__':
    create_db()
    app.run()
