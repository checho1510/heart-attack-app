from flask import Flask, jsonify, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)

@app.route('/')
def hello_world():
    #test = [34, 0, 200, 0, 60, 0, 300000, 1000, 140, 1, 0]
    test_bad = [80, 1, 7861, 1, 20, 1, 850000, 2.7, 110, 1, 1]
    model = load('model.joblib')
    test_pred = model.predict_proba(np.array([test_bad]))
    return jsonify(test_pred.tolist())

@app.route('/index', methods=['GET', 'POST'])
def index():
    req_method = request.method
    if req_method == 'GET':
        return render_template('index.html', result="")
    else:
        age = int(request.form['age'])
        anemia = int(request.form['anemia'])
        creatina_quin = int(request.form['creatina_quin'])
        diabetes = int(request.form['diabetes'])
        eyection = int(request.form['eyection'])
        hpb = int(request.form['hpb'])
        plaquetas = float(request.form['plaquetas'])
        creatina = float(request.form['creatina'])
        sodio = int(request.form['sodio'])
        sex = int(request.form['sex'])
        smoke = int(request.form['smoke'])

        test = [age, anemia, creatina_quin, diabetes,
                    eyection, hpb, plaquetas, creatina,
                    sodio, sex, smoke]
        model = load('model.joblib')
        test_pred = model.predict_proba(np.array([test]))

        value = round(test_pred[0,1] * 100, 1)

        return render_template('index.html', result= str(value) + '%')
    


