from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import requests as req


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        r = req.post("http://www.sis.nileuniversity.edu.ng/my/loginAuth.php", data={"username": student_id, "password": password, "LogIn": "LOGIN"})
        res = r.content.decode()
        print(res.find("incorrect") == -1)
        if res.find("incorrect") == -1:
            str_to_find = '<h4 class="card-title m-t-10">'
            idx = res.find(str_to_find)+len(str_to_find)
            new_sub_str = res[idx:idx+100].replace("</h4>", "")
            all_names = new_sub_str.split()
            name = all_names[0] + " " + all_names[2]
            user = User.query.filter_by(name=name).first()
            if not user:
                user = User(name=name)
                db.session.add(user)
                db.session.commit() 
            login_user(user, True)
            return redirect(url_for('views.home'))
        else:
            flash('Wrong student ID or password', 'danger')
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
