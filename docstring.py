def home_string(self):
    """
    Homepage
    ________

    User is shown login screen at start

    Parameters:
    username(string): User enters registered username
    password(string): User enters registered password

    Returns:
    new homepage: Shows user's lists of finished and unfinished tasks

    """

    return self

print (home_string.__doc__)


def add_string(self):
    """
    Add task
    ________

    User is allowed to input and save task information

    Parameters:
    description(string): Name of task
    content(string): Description of task
    deadline(date/time): Date and time of task

    Returns:
    new item: Task is now added to "unfinished task" list

    """

    return self

print (add_string.__doc__)


def edit_string(self):
    """
    Edit task
    _________

    User is allowed to edit existing tasks

    Parameters:
    description(string): Name of task
    content(string): Description of task
    deadline(date/time): Date and time of task

    Returns:
    edited item: Edited task replaces old task

    """

    return self

print (edit_string.__doc__)


def finish_string(self):
    """
    Finish task
    ___________

    User can mark a task as finished by clicking the checkmark icon

    Parameters:
    finished(boolean): Check if task is marked as finished

    Returns:
    moved item: Finished tasks moves to "finished tasks" list

    """

    return self

print (finish_string.__doc__)


def share_string(self):
    """
    Share task
    __________

    User can choose tasks to share with another user

    Parameters:
    task(data): Task(s) is chosen for sharing
    email(string): User enters the email to share tasks with

    Returns:
    email pdf: A pdf of the chosen tasks is sent to the other user

    """

    return self

print (share_string.__doc__)


def profile_string(self):
    """
    Profile
    _______

    User can check their account information

    Parameters:
    None

    Returns:
    None

    """

    return self

print (profile_string.__doc__)


def contact_string(self):
    """
    Contact form
    ____________

    User can send a contact form to developers regarding the application

    Parameters:
    name(string): User's name
    email(string): User's login email
    subject(string): Subject for the contact form
    message(string): Description of the subject'

    Returns:
    None

    """

    return self

print (contact_string.__doc__)
