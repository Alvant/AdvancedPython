import os

from flask import (
    Flask, render_template, request, session
)

from json_database import JsonDatabase



app = Flask(
    __name__,
    static_url_path='/static',
    template_folder='./site/templates',
    static_folder='./site/static'
)
app.secret_key = os.urandom(24)

db = JsonDatabase('./comments.txt')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recipes/apply_pie', methods=('GET', 'POST'))
def apple_pie():
    # TODO: it is possible to send the same comment several times
    #  (after page refresh)

    if request.method == 'POST':
        new_comment = request.form['comment']
        db.save_comment(new_comment)

    comments_text = _compose_comments_text(db.comments)
    session['comments'] = db.comments

    # TODO: many comments -> bad for memory (do we really need session?)

    return render_template(
        'recipe.html',
        comments_text=comments_text
    )


def _compose_comments_text(comments):
    return '\n' + '\n\n'.join(
        [f'[{c[1]}]: {c[0]}' for c in comments]
    )



if __name__ == '__main__':
    app.run(debug=True)

