from flask import Flask, render_template


app = Flask(
    __name__,
    static_url_path='/static',
    template_folder='./site/templates',
    static_folder='./site/static'
)


@app.route('/')
@app.route('/recipes/apple_pie')
def home_page():
    return render_template('recipe.html')


if __name__ == '__main__':
    app.run(debug=True)

