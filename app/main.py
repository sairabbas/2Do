from flask import render_template, url_for, redirect, flash, request, make_response
from app import app, db
from app.form import signin, register, createTask, createList, contactForm, shareForm
from flask_login import logout_user
from flask_login import login_required, current_user, login_user
from werkzeug.urls import url_parse
from app.models import User, Todo, newList
from app.function import transformForm, HTML2PDF,sttShareFalse



# ________________________________________________________________________________________
# for sending mail
from flask_mail import Message, Mail


# ________________________________________________________________________________________
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "2dowebsite2do@gmail.com"
app.config["MAIL_PASSWORD"] = "2dowebsite"

mail.init_app(app)

# ________________________________________________________________________________________
@app.route("/")
@app.route("/home")
@login_required
def home():
    todo = Todo.query.all()
    newlist = newList.query.all()
    return render_template("home.html", newlist=newlist, todo=todo, title="HOME")


# ________________________________________________________________________________________


@app.route("/login")
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = signin()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            flash(f"Login successfully for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("signin.html", title="Sign In", form=form)


# ________________________________________________________________________________________
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/register")
@app.route("/register", methods=["GET", "POST"])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = register()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account successfully created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Sign Up")


# ________________________________________________________________________________________
# Error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # all objects are expired
    return render_template("500.html"), 500


# ________________________________________________________________________________________
# list page
@app.route("/list", methods=["GET", "POST"])
@login_required
def newlist():
    form = createList()
    if request.method == "POST":
        name = request.form.get("name")
        newname = newList(name=name, user=current_user._get_current_object())
        db.session.add(newname)
        db.session.commit()
        flash("List successfully created!", "success")
        return redirect("home")

    return render_template("home.html", title="HOME")


# ________________________________________________________________________________________
# add tasks
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    form = createTask()

    if request.method == "POST":
        description = request.form.get("description")
        content = request.form.get("content")
        # get the value of datetime in the form of html and then change the HTML's format to DB's format
        deadline = request.form.get("deadline")
        deadline = transformForm(deadline)
        # inserting the inputs to the database
        todo = Todo(
            description=description,
            content=content,
            deadline=deadline,
            status=False,
            statusShare=True,
            user=current_user._get_current_object(),
        )
        db.session.add(todo)
        db.session.commit()
        flash("Task successfully created!", "success")

        # flash('Successfully to create task!', 'success')

        return redirect(url_for("home"))
        # posts = Todo.query.order_by(Todo.timestamp.desc()).all()
    return render_template("tasks.html", form=form, legend="New Tasks", title="add")


# ________________________________________________________________________________________
# complete tasks
@app.route("/complete/<int:id>")
@login_required
def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.status = True
    db.session.commit()
    return redirect(url_for("home"))


# ________________________________________________________________________________________
# delete tasks
@app.route("/delete/<int:id>")
@login_required
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/deleteList/<int:id>")
@login_required
def deleteList(id):
    newlist = newList.query.filter_by(id=id).first()
    db.session.delete(newlist)
    db.session.commit()
    return redirect(url_for("home"))


# ________________________________________________________________________________________
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    todo = Todo.query.filter_by(id=id).first()
    form = createTask()
    u = todo.deadline.strftime("%Y-%m-%dT%H:%M")  # reformat the db to html
    if request.method == "POST":
        todo.description = request.form.get("description")
        todo.content = request.form.get("content")
        deadline = request.form.get("deadline")
        todo.status = form.status.data
        deadline = transformForm(deadline)
        todo.deadline = deadline
        db.session.commit()
        flash("Updated Successfully", "success")
        return redirect(url_for("home"))
    return render_template(
        "tasks.html", title="Edit", legend="Edit Tasks", u=u, form=form, todo=todo
    )


# ________________________________________________________________________________________
@app.route("/profile/<string:username>")
@login_required
def info(username):
    yourInfo = User.query.filter_by(username=username).first_or_404()
    todo = Todo.query.all()
    return render_template(
        "profile.html", title="Profile", todo=todo, yourInfo=yourInfo
    )


# ________________________________________________________________________________________
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = contactForm()
    if request.method == "POST":
        msg = Message(
            form.subject.data,
            sender=form.email.data,
            recipients=["2dowebsite2do@gmail.com"],
        )
        msg.body = """
            Customer: 
                Name: %s  
                Email:  %s 
                Message: %s 
            """ % (
            form.name.data,
            form.email.data,
            form.message.data,
        )
        mail.send(msg)
        flash("Thank you for your message. We'll get back to you shortly.", "success")
        return redirect(url_for("home"))

    return render_template("contact.html", form=form)


# ________________________________________________________________________________________
@app.route("/sharing", methods=["GET", "POST"])
@login_required
def share():
    form = shareForm()
    todo = Todo.query.all()
    if request.method == "POST":
        emailReceiver= request.form.get("emailReceiver")
        check = request.form.getlist("Check")

        #change the status of share which the user wants to share
        for x in check:
            todo1 = Todo.query.filter_by(id=x).first()
            todo1.statusShare=True
        db.session.commit()

        #create the pdf, convert html to pdf
        rendered = render_template("mail.html", form=form, todo=todo)
        pdf = HTML2PDF()  # in function.py (class)
        pdf.add_page()
        pdf.write_html(rendered)
        # pdf output, PDF data output as a string
        response = pdf.output(dest='S')

        #gmail structure
        msg = Message(
            "2DO SHARING",
            sender="2dowebsite2do@gmail.com",
            recipients=[emailReceiver],
        )
        msg.body = """
        2DO SHARING
            """
        # for attach the file
        msg.attach(
            "2DO",'application/pdf',response)

        #UI for the mail
        msg.html = rendered

        #Send msg
        mail.send(msg)
        # recover the share status to False
        sttShareFalse(check)
        flash("Sent successfully", "success")
        return redirect(url_for('home'))
    return render_template("home.html", form=form, todo=todo)




if __name__ == "__main__":
    app.run(debug=True)
