from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.template.html')
    
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.template.html')
    
@app.route('/typography')
def typography():
    return render_template('typography.template.html')
    
@app.route('/blog-leftsidebar')
def blogLeftsidebar():
    return render_template('blog-leftsidebar.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)