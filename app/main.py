from flask import render_template, url_for, redirect, flash, request
from app import app, db
from app.form import signin, register, createTask
from flask_login import logout_user
from flask_login import login_required, current_user, login_user
from werkzeug.urls import url_parse
from app.models import User, Todo
'''
TODO: 
1. fix or add the variable  comlumn  into database (models.py) (time)
3. create DB for friends of the users (models.db), email, design page (html, css)
4. function share by email
Note: You can create account for your own
'''
@app.route('/')
@app.route('/home')
@login_required
def home():
    todos = Todo.query.all()
    return render_template('home.html', todos = todos,  title='HOME')

@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = signin()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password','danger')
                return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('signin.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/register")
@app.route("/register", methods=['GET', 'POST'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = register()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Successfully to create for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form, title="Sign Up")

# Error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback() # all objects are expired
    return render_template('500.html'),500

#add tasks
@app.route('/add', methods =['GET','POST'])
@login_required
def add(): 
    form = createTask()

    if form.validate_on_submit():
        todo = Todo(description = form.description.data, status=False)
        db.session.add(todo)
        db.session.commit()
        flash('Successfully to create task!', 'success')
        return redirect(url_for('home'))
    return render_template('tasks.html',form=form, legend = 'New Tasks', title="add")

#complete tasks
@app.route('/complete/<int:id>')
def complete(id): 
    todo = Todo.query.filter_by(id = id).first()
    todo.status = True
    db.session.commit()
    return redirect(url_for('home'))

#delete tasks
@app.route('/delete/<int:id>')
def delete(id): 
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id): 
    todo = Todo.query.filter_by(id = id).first()
    form = createTask()
    if  form.validate_on_submit(): 
        todo.description = form.description.data
        db.session.commit()
        # todo.deadline = form.deadline.data
        flash('Updated Successfully', 'success')
        return redirect(url_for('home', id = id))
    elif request.method == 'GET':
        form.description.data = todo.description
        form.status.data = todo.status
        # form.deadline.data = todo.deadline
    return render_template('tasks.html', title='Edit', legend = 'Edit Tasks', form= form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
