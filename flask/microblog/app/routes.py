from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm

import json

@app.route('/')
def home():
    return render_template('index.html')

i = 0

@app.route('/adventure', methods=['GET', 'POST'])
def login():
    global i 
    with open("content.json") as file:
        content = json.load(file)

    form = LoginForm()
    numScenarios = len(content["content"])-1
    if form.validate_on_submit(): 
        if i==numScenarios: 
            return render_template('end.html', title='Amagon End', form=form, content=content, i=i)
        if form.choice_A.data and form.choice_B.data: 
            flash("Please pick one answer only!!")
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i)
        if form.choice_A.data: 
            return render_template('adventure.html', title='A', form=form, content=content, i=i)
        elif form.choice_B.data: 
            return render_template('adventure.html', title='B', form=form, content=content, i=i)   
        else: 
            i += 1
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 
    else:
        return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 

