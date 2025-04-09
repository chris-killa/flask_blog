import os
import json

DATA_FILE = os.path.join('data', 'posts.json')

def load_posts():
    if not os.path.exists(DATA_FILE):
        example_posts = [
            {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
            {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'}
        ]
        save_posts(example_posts)  # direkt speichern
        return example_posts
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_posts(posts):
    with open(DATA_FILE, 'w') as f:
        json.dump(posts, f, indent=4)