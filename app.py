import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    
    int_features = [int(x) for x in request.form.values()]
    int_features.append(1)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction[0] ==1.0:
        output ='Exited'
    else:
        output = 'Not Exited'
    


    return render_template('index.html', prediction_text='**********Bank Customer is  {}**********'.format(output))


if __name__ == "__main__":
    app.run(use_reloader=False, debug=True)
