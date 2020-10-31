from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}, choice_A={}, choice_B={}'.format(
            form.username.data, form.remember_me.data, form.choice_A.data, form.choice_B.data))
        print("Login accepted. Redirecting to Home")
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
