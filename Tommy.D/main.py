from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("card 0", "A great destination!!!", "link", "static/images/Untitled.png"),
        ("card 1", "One of the natural wonders of the world", "link", "static/images/logo.card1"),
        ("card 2", "some text", "Button text", "static/images/logo.card1"),
        ("card 3", "some text", "Button text", "static/images/logo.card1"),
    )
    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)