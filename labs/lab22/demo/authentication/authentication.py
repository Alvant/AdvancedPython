import os

from flask import Blueprint, render_template, request

from db import JsonDatabase


# TODO: path -- in config
database = JsonDatabase(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data',
        'db.txt'
    )
)

blueprint = Blueprint(
    name='authentication',
    import_name=__name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=("GET", "POST"))
def register():
    if request.method == 'GET':
        return render_template('login.html')

    database.save(
        username=request.form['username'],
        password=hash(
            request.form['password']
        )
    )

    return render_template('success.html')


@blueprint.route('/login', methods=("GET", "POST"))
def login():
    if request.method == 'GET':
        return render_template('login.html')

    try:
        user = database.find(username=request.form['username'])
    except KeyError:
        return render_template('fail.html')

    if user['password'] == hash(request.form['password']):
        return render_template('success.html')
    else:
        return render_template('fail.html')
