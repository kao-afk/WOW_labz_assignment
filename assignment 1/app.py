from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        file_name = "model.pkl"
        reg = pickle.load(open(file_name, "rb"))
        out = np.round(reg.predict([[time]])[0],2)
        data1 = {"name":name,"time":time, "out":out}
        return render_template('success.html',data = data1)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
