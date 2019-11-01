from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

msg = []

@app.route('/')
def index():
	return render_template('index.template.html', messages = msg)

@app.route('/', methods=['POST'])
def add_message():
  new_message = request.form['new-message']
  msg.append(new_message)
  return redirect('/')

    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)