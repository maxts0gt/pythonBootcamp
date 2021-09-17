from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
app.url_map.strict_slashes = False

posts = requests.get("https://api.npoint.io/642505b5e19731d16268").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"],
                    post["body"], post["author"], post["dates"])
    post_objects.append(post_obj)


@app.route('/index.html')
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@ app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@ app.route('/about.html')
def about():
    return render_template("about.html")


@ app.route('/contact.html')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
