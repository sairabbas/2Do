from flask import Flask, render_template, redirect, request, flash, redirect
from form import register, signin

app = Flask(__name__)
app.config["SECRET_KEY"] = "AL"
nameUser = "Anh"


@app.route("/")
@app.route("/Home")
def home():
    return render_template("home.html", name=nameUser, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/blog")
def blog():

    return render_template("blog.html", title=nameUser, post=posts)


@app.route("/blog/<string:blog_id>")
def blogpost(blog_id):
    return "Blog Post Number " + blog_id


@app.route("/register", methods=["GET", "POST"])
def signUp():
    form = register()
    if form.is_submitted():
        result = request.form
        return render_template("user.html", result=result)
    return render_template("register.html", form=form, title="Sign Up")


@app.route("/signin", methods=["GET", "POST"])
def signIn():
    form = signin()
    if form.validate_on_submit():
        return render_template(redirect(home()))
    return render_template("signin.html", form=form, title="Sign In")


if __name__ == "__main__":
    app.run(debug=True)

