[![Build Status](https://travis-ci.com/hamsikapongubala/CMPE131.svg?branch=master)](https://travis-ci.com/hamsikapongubala/CMPE131)

# 2Do by Team 9
Alvin Huang, Anh Le, Hamsika Pongubala, Sair Abbas

## About the App:

2Do is a task management application, which will allow users to manage their daily task with ease. The app will allow users to enter their daily tasks, set notification timings, create new to do lists, and share their tasks with other 2Do users! Our hope is that managing your daily schedule becomes easier.

## Features

The following features are implemented:

- [x] User can register
- [x] User can login
- [x] User can create a task
- [x] User can edit a task
- [x] User can delete a task
- [x] User can create a new list
- [x] User can contact to the admin
- [x] User can share tasks to others by email
- [x] Application side the database securely contains user information
- [x] User interface designed using bootstrap.

## How to get started!

Required Software: PyCharm CE, Python3, Google Chrome

Run the command on terminal

    git clone git@github.com:hamsikapongubala/CMPE131.git
    
Or Directly Download the project onto your local computer by clicking the Clone or Download button on the top right.

Change directory to the downloaded folder. Then run the commands on terminal:
        
    export FLASK_APP=myApp.py
    flask run

Alternative method is to use pycharm. Then run the command on the terminal in PyCharm:

    flask run

A url will be created for you to run locally on your computer, use this url on your web browser:

    Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Register yourself as a user and start using 2Do!

## How to verify features:

### Register

To access the application a user must register themselves. By clicking the sign up now button on the bottom sign in page will redirect them to the register page. Users can register as a new user with a username, password, and an email. 

### Login 

After registering as a user, users can login in with the same credentials. This can allow the users to access the app with their finished and unfinished tasks lists, associated with their account.

### Create a Task

On the top right corner there is a create a task tab, which will redirect you to a page to add a new task                  with a title, content description, and due date. Creating a task will add the task to the users 'unfinished tasks' list.

### Edit a task

On clicking the edit a task link on an exisiting task, the user can edit the description, content, and notification date. The updates will then be updated home page under the 'unfinished tasks' list.

### Delete a task

On clicking the delete link on an exisiting task, the user can delete the task. This option is not reversible and the task will be removed from the users list entirely.

### Create a list

On clicking the create a list tab on the navigation bar, the user will be redirected to a webpage to insert the list title. This allows the user to create a list on the homepage other than the default 'unfinished tasks' and 'finished tasks'.

### Contact

On clicking the contact link on navigation bar, users can contact  the admin of the app to have questions or ideas. In the short time, the customer service will send the reply back to email of  the users. 

### Share

On clicking the share link on navigation bar, users can  share the tasks to others' email. 


### Database

The database containing user login information, user tasks, and lists are currently being stored on the database. This enables the user login to their home page and have their information associated with their account only. 

### Bootstrap

The styling of all the webpages was done using bootstrap and CSS.
