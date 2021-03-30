from flask import Flask, render_template

from authentication.authentication import blueprint as auth_blueprint

app = Flask(__name__)
app.register_blueprint(
    auth_blueprint
)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
