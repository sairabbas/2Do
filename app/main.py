from flask import render_template, url_for, redirect, flash, request
from app import app, db
from app.form import signin, register, createTask, createList
from flask_login import logout_user
from flask_login import login_required, current_user, login_user
from werkzeug.urls import url_parse
from app.models import User, Todo
from app.function import transformForm

@app.route('/')
@app.route('/home')
@login_required
def home():
    todo = Todo.query.all()
    return render_template('home.html', todo=todo,  title='HOME')

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
        flash(f'Account successfully created for {form.username.data}!', 'success')
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

#list page
@app.route('/newList')
@login_required
def newList():
    form = createList()
    name = request.form.get('name')
    return render_template('newList.html',form=form)


#add tasks
@app.route('/add', methods =['GET','POST'])
@login_required
def add(): 
    form = createTask()

    if request.method == 'POST' :
        description  = request.form.get('description')
        content = request.form.get('content')
        # get the value of datetime in the form of html and then change the HTML's format to DB's format
        deadline = request.form.get('deadline')
        deadline = transformForm(deadline)
        # inserting the inputs to the database
        todo = Todo(description = description, content = content, deadline = deadline,  status=False, user=current_user._get_current_object())
        db.session.add(todo)
        db.session.commit()
        db.session.query(Todo)
        flash('Task successfully created!', 'success')

       # flash('Successfully to create task!', 'success')

        return redirect(url_for('home'))
        # posts = Todo.query.order_by(Todo.timestamp.desc()).all()
    return render_template('tasks.html',form=form, legend = 'New Tasks', title="add")

#complete tasks
@app.route('/complete/<int:id>')
@login_required
def complete(id): 
    todo = Todo.query.filter_by(id = id).first()
    todo.status = True
    db.session.commit()
    return redirect(url_for('home'))

#delete tasks
@app.route('/delete/<int:id>')
@login_required
def delete(id): 
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id): 
    todo = Todo.query.filter_by(id = id).first()
    form = createTask()
    u = todo.deadline.strftime('%Y-%m-%dT%H:%M') #reformat the db to html
    if request.method == 'POST':
            todo.description = request.form.get('description')
            todo.content =  request.form.get('content')
            deadline =  request.form.get('deadline')
            todo.status = form.status.data 
            deadline = transformForm(deadline)
            todo.deadline = deadline
            db.session.commit()
            flash('Updated Successfully', 'success')
            return redirect(url_for('home'))
    return render_template('tasks.html', title='Edit', legend = 'Edit Tasks',u=u, form =form, todo = todo)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
