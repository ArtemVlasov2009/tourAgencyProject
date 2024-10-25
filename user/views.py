import flask, flask_login
from .models import Users
from main.settings import DATABASE
from main.settings import project
from flask_login import current_user
def render_user():
    if flask.request.method == "POST":
        if current_user.is_authenticated:
            print("logout in process")
            flask_login.logout_user()
            return flask.redirect("/login")
                
    return flask.render_template(template_name_or_list="user.html", current_user = current_user)

is_registered = False
def render_registration():
    global is_registered
    if flask.request.method == "POST":
        password = flask.request.form['password']

        if len(password) < 6:
            return("Enter at least 6 characters")
        
        user = Users( 
            username = flask.request.form["username"],
            password = password
        )

        if current_user.is_authenticated:
            return "You are already authorized"

        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            is_registered = True
            return flask.redirect("/login")
            
        except:
            return "error"
        
            
    return flask.render_template(template_name_or_list="registration.html", is_registered = is_registered)



def render_login():
    global is_registered
    if flask.request.method == "POST":
        

        for user in Users.query.filter_by(username = flask.request.form.get("username")):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect("/profile")
        
        if is_registered == False:
            return "You are not authorized"
        


    return flask.render_template(template_name_or_list="login.html", is_registered = is_registered)

def render_welcome():
    if flask.request.method == "POST":
        if current_user.is_authenticated:
            print("logout in process")
            flask_login.logout_user()
            return flask.redirect("/login")
    
    return flask.render_template(template_name_or_list="profile.html", username = current_user.username, current_user = current_user )