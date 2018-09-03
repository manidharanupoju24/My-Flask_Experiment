from flask import Flask


app = Flask(__name__)
posts = {
    0 : {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')  # /post/0 tag is flask syntax
def post(post_id):
    post = posts.get(post_id)
    return f"Post : {post['title']}, content : \n\n{post['content']}"


if __name__ == '__main__':
    app.run(debug=True)