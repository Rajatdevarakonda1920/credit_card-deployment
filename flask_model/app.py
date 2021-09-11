from flask import Flask,render_template,request
import joblib

#intiliaze the app
app = Flask(__name__)
model = joblib.load(r'C:\Users\RAJAT DEVARAKONDA\Desktop\Data_Science\PROJECTS DEPLOYMENTS\credit_card\flask_model\credit_crd.pkl')
print('[INFO] model loaded')

#__name__ refers that this file main file in the module

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict' , methods = ['post'])
def predict():
    LIMIT_BAL = request.form.get('LIMIT_BAL')
    EDUCATION = request.form.get('EDUCATION')
    MARRIAGE = request.form.get('MARRIAGE')
    PAY_0 = request.form.get('PAY_0')
    PAY_2 = request.form.get('PAY_2')
    PAY_3 = request.form.get('PAY_3')
    PAY_4 = request.form.get('PAY_4')
    PAY_5 = request.form.get('PAY_5')
    PAY_6 = request.form.get('PAY_6')
    PAY_AMT1 = request.form.get('PAY_AMT1')
    PAY_AMT2 = request.form.get('PAY_AMT2')
    PAY_AMT3 = request.form.get('PAY_AMT3')
    PAY_AMT4 = request.form.get('PAY_AMT4')
    PAY_AMT5 = request.form.get('PAY_AMT5')
    PAY_AMT6 = request.form.get('PAY_AMT6')

    print(LIMIT_BAL,EDUCATION,MARRIAGE,PAY_0,PAY_2, PAY_3,PAY_4,PAY_5,PAY_6,PAY_AMT1, PAY_AMT2, PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
    output = model.predict([[LIMIT_BAL,EDUCATION,MARRIAGE,PAY_0,PAY_2, PAY_3,PAY_4,PAY_5,PAY_6,PAY_AMT1, PAY_AMT2, PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]])
    if output[0]==1:
        print('Cutomer Will DEFAULT')
        result = 'DEFAULT'
    else:
        print('Cutomer Will Not DEFAULT')
        result = 'Not DEFAULT'
    return render_template('predict.html',predict=f'Customer Will {result}')


# run the app
app.run(debug=True)


