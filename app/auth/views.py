from flask import (render_template, redirect, url_for,flash, request)
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import SignUpForm, LoginForm
from .. import db
# from ..email import mail_message

@auth.route("/signup", methods = ["GET", "POST"])
def register():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        user = User(first_name = signup_form.first_name.data, last_name = signup_form.last_name.data,username = signup_form.username.data, email = signup_form.email.data,password = signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("auth.login"))
    title = "Sign Up to 60 Seconds"
    return render_template("auth/signup.html", signup_form = signup_form,title = title)