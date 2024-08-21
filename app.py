#importing the libraries
from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import pickle

print(pd.__version__, np.__version__)
app = Flask(__name__, template_folder='templates')

#import the model
loaded_model = pickle.load(open('./car_price_predicition1.model','rb'))

#load the data
car=pd.read_csv('./Cleaned_data.csv')

model = loaded_model['model']
scaler= loaded_model['scaler']
brand_le = loaded_model['brand_le']
year_default = loaded_model['year_default']
max_power_default = loaded_model['max_power_default']
mileage_default = loaded_model['mileage_default']


@app.route('/')
def index():
    brand = sorted(car['brand'].unique())
    year = sorted(car['year'].unique(),reverse=True)
    max_power = car['max_power']
    mileage = car['mileage']
    
    return render_template('index.html',brand=brand, year=year, max_power=max_power, mileage=mileage)


@app.route('/predict',methods=['POST'])
def predict():

    brand_name = request.form.get('brand')
    brand = brand_le.transform([brand_name])
    year = request.form.get('year')
    max_power = float(request.form.get('max_power'))
    mileage = float(request.form.get('mileage'))
    
    sample_np = np.array([[brand[0],year,max_power,mileage]])
    
    sample = scaler.transform(sample_np)

    predicted_result = np.exp(model.predict(sample))
    return str(int(predicted_result[0]))



if __name__ == '__main__':
    app.run(debug=True, port=5001)

    
