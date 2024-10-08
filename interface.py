from flask import Flask,render_template,jsonify,request
# from test import add
from Project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route('/') #HomeAPI
def hello_Flask():
    print("Welcome to Flask")
    return "Hello Python"

@app.route('/predict_charges')
def get_insurance_charges():
    
    data = request.form
    print('Data is:',data)
    
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    print('')    
    
    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()
    
    return jsonify({'Result':f"Predicted Medical Insurance Charges: {charges}"})

app.run(debug=True)

# app.run(host='',port=config,PORT_NUMBER,debug='False')
# host to give url, port number to give sp. port number 1hr:00