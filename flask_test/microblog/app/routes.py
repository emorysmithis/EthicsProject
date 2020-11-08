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
    #print(content)

    form = LoginForm()
    numScenarios = len(content)
    print("Number of Scenarios: {}".format(numScenarios))
    if form.validate_on_submit(): 
        flash("You pressed submit")
        if i==numScenarios: 
            return render_template('end.html', title='Amagon End', form=form, content=content, i=i) 
        if form.choice_A.data: 
            print("on scenario {}".format(i)) 
            flash('You selected Choice A')  
            return render_template('adventure.html', title='A', form=form, content=content, i=i)
            print('After showing A page') 
        elif form.choice_B.data: 
            print("on scenario {}".format(i)) 
            flash('You selected Choice B') 
            return render_template('adventure.html', title='B', form=form, content=content, i=i)   
            print('After showing B page')
        else: 
            i += 1
            return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 
    else:
        print("i on loading initial page:{}".format(i))
        return render_template('adventure.html', title='Amagon', form=form, content=content, i=i) 

