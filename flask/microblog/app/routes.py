from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm

import json

@app.route('/')
def home():
    return render_template('index.html')

i = 0
scenario_page = 0

@app.route('/adventure', methods=['GET', 'POST'])
def login():
    global i 
    global scenario_page
    with open("content.json") as file:
        content = json.load(file)

    form = LoginForm()
    numScenarios = len(content["content"])-1
    if form.validate_on_submit(): 
        if i==numScenarios: 
            return render_template('end.html', title='Amagon End', form=form, content=content, i=i)
        if scenario_page and not form.choice_A.data and not form.choice_B.data:
            scenario_page = 1 
            flash("Please pick an answer!") 
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i)
        if (form.choice_A.data and form.choice_B.data): 
            scenario_page = 1 
            flash("Please pick one answer only!!")
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i)
        if form.choice_A.data: 
            scenario_page = 0 
            return render_template('adventure.html', title='A', form=form, content=content, i=i)
        elif form.choice_B.data: 
            scenario_page = 0 
            return render_template('adventure.html', title='B', form=form, content=content, i=i)   
        else: 
            i += 1
            scenario_page = 1
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 
    else:
        scenario_page = 1 
        return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 

