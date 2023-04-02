import os

from typing import List

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    # session  # For cookies
)

from db import (
    Comment,
    CommentsDatabase,
)


app = Flask(
    __name__,
    static_url_path='/static',
    template_folder='./templates',
    static_folder='./static'
)
# app.secret_key = os.urandom(24)  # For cookies

db = CommentsDatabase('./_comments.txt')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recipes/apply_pie', methods=('GET', 'POST'))
def apple_pie():
    if request.method == 'POST':
        new_comment = request.form['comment']
        db.save_comment(new_comment)

        # redirect prevents duplicate POST after page refresh
        return redirect(url_for('apple_pie'))

    comments_text = _compose_comments_text(db.comments)
    # session['comments'] = db.comments

    return render_template(
        'recipe.html', comments_text=comments_text
    )


def _compose_comments_text(comments: List[Comment]):
    return '\n' + '\n\n'.join(
        [f"[{c.date}]: {c.text}" for c in comments]
    )



if __name__ == '__main__':
    app.run(debug=True)

