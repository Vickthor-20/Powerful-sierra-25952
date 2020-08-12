# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:45:29 2020

@author: USUARIO
"""


from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    """return 'Hello World'"""
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('About.html')

if __name__=='__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)
    
    
    
    