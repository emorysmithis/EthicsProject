from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    posts = [ 
        { 
            'choice': {'choice':'A'}, 
            'body': 'This is choice A!'
        }, 
        { 
            'choice': {'choice': 'B'}, 
            'body': 'This is choice B!'
        }
    ]
    form = LoginForm()
    if form.validate_on_submit():
        flash("You pressed submit")
        if form.choice_A.data: 
            flash('You selected Choice A')  
        else: 
            flash('You seected Choice B') 
    return render_template('login.html', title='Amagon', form=form, posts=posts) 

