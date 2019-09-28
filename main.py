from flask import Flask, render_template, redirect, request, flash, redirect
from form import register, signin

app = Flask(__name__)
app.config["SECRET_KEY"] = "2Do"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

# TODO: register and sign in need to input the 2 def validate() on each for checking the account is valid or not (username, email), but it needs database to check the account.
# register page
@app.route("/register", methods=["GET", "POST"])
def signUp():
    form = register()
    return render_template("register.html", form=form, title="Sign Up")

# sign in page
@app.route("/signin", methods=["GET", "POST"])
def signIn():
    form = signin()
    if form.validate_on_submit():
        return render_template(redirect(home()))
    return render_template("signin.html", form=form, title="Sign In")

# create task
@app.route('/tasks', methods=('GET','POST'))
def tasks():

    title='Tasks'
    form = CreateTask()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('tasks.html',form=form,title=title)

if __name__ == '__main__':
    app.run(debug=True)

