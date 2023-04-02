from flask import Flask, render_template


app = Flask(
    import_name=__name__,
    static_url_path='/static',
    template_folder='./templates',
    static_folder='./static'
)


@app.route('/')
@app.route('/recipes/apple_pie')
def home_page():
    return render_template('recipe.html')


@app.route('/_test')
def test():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

