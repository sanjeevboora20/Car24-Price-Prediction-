# ! pip install Flask
from flask import Flask, render_template, request
import pickle
from markupsafe import escape
from jinja2 import escape

app = Flask(__name__)
model = pickle.load(open('m3.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

# company - 18 differnt values
# Car_Name - 83 different values
# mnf_year - 2008-2022
# fuel-type - 0,1,2

@app.route("/predict", methods=['POST'])
def predict():
    comp = float(request.form['Company'])
    car_name = float(request.form['Car_Name'])
    owner = float(request.form['owner'])
    mnf_year = float(request.form['mnf_year'])
    fuel_type = float(request.form['Fuel_Type'])
    kms_driven = float(request.form['kms_driven'])
    y_pred = model.predict([[comp,car_name,owner,mnf_year,fuel_type,kms_driven]])[0]
    return render_template('index.html', prediction_text=y_pred)

if __name__ == "__main__":
    app.run()