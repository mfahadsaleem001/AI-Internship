from flask import Flask , jsonify

app = Flask(__name__)


posts = [
    {
        "id": 1,
        "title": "AI Agents",
        "author": "Mr Subhan"
    },
    {
        "id": 2,
        "title": "Python Basics",
        "author": "Mr Afaq"
    }
]

@app.route("/posts")
def get_posts():
    return jsonify(posts)

@app.route("/posts/<int:id>")
def get_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify(post)

    return jsonify({"error": "Post not found"}), 404

if __name__ == "__main__":
    app.run()