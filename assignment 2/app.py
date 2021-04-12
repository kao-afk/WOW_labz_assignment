from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import model

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        book = request.form['time']
        t='His name is Dr. K. R. Singh. Dr. K. R. Singh is a student in the department of geology There is a growth of 10.67.67 in business. He is a student in the department of geology. There is a growth of 10.67 in business.'
        sentiment , sentences , first , second = model.model_call(name)
        output = []
        for x,y in zip(sentences,sentiment):
            output.append([x,y])
        data1 = {"name":name,"book":book}
        return render_template('success.html',data = data1,outs = output, first = first , second = second)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
