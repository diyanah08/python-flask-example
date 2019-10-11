from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.template.html')
    
@app.route('/', methods = ["POST"])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight / (height * height)
    return "BMI = " + str(bmi)
    
# @app.route('/', methods = ["GET", "POST"])
# if request.methods == ["GET"]:
#     return render_template('index.template.html')
# elif request.methods == ["POST"]:
#     def calculate_bmi():
#         weight = float(request.form['weight'])
#         height = float(request.form['height'])
#         bmi = weight / (height * height)
#         return "BMI = " + str(bmi)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)