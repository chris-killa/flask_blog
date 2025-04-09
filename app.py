from flask import Flask, render_template, request
from data.storage import load_posts
app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004, debug=True)