from flask import Flask, render_template, request, redirect, url_for
from data.storage import load_posts, save_posts

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = load_posts()
        new_post = {
            "id" : len(blog_posts)+1,
            "title" : request.form.get('title'),
            "content" : request.form.get('content'),
            "author" : request.form.get('author'),
            "likes" : request.form.get('likes', 0)
        }
        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts = load_posts()
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    save_posts(blog_posts)
    return redirect(url_for('index'))

@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    blog_posts = load_posts()
    post = next((p for p in blog_posts if str(p['id']) == str(post_id)), None)
    if post is None:
        return "Post not found", 404
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        post['author'] = request.form['author']
        post['likes'] = 0
        save_posts(blog_posts)
        return redirect(url_for('index'))
    return render_template('index.html', post=post)

@app.route('/like/<int:id>',  methods=['POST'])
def like(id):
    blog_posts = load_posts()
    post = next((p for p in blog_posts if str(p['id']) == str(id)), None)
    if request.method == 'POST':
        post['likes'] += 1
        save_posts(blog_posts)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004, debug=True)