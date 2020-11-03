from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm

import json

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adventure', methods=['GET', 'POST'])
def login():
    with open("content.json") as file:
        content = json.load(file)

    posts = [ 
        { 
            'choice': {'choice':'A'}, 
            'body': 'This is choice A!', 
            'consequence': 'This is the consequence for Choice A'
        }, 
        { 
            'choice': {'choice': 'B'}, 
            'body': 'This is choice B!', 
            'consequence': 'This is the consequence for Choice B'
        }
    ]
    form = LoginForm()
    if form.validate_on_submit():
        flash("You pressed submit")
        if form.choice_A.data: 
            flash('You selected Choice A')  
            return render_template('adventure.html', title='A', form=form, posts=posts, content=content)
            print('After showing A page') 
        elif form.choice_B.data: 
            flash('You selected Choice B') 
            return render_template('adventure.html', title='B', form=form, posts=posts, content=content)   
            print('After showing B page')
        else: 
            return render_template('adventure.html', title='Amagon', form=form, posts=posts, content=content) 
    else: 
        return render_template('adventure.html', title='Amagon', form=form, posts=posts, content=content) 

