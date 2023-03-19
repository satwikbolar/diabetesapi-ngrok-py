import json
import requests

url = 'http://f0e1-35-243-153-160.ngrok.io/diabetes_prediction'

input_data_for_model = {
  'Pregnancies': 5,
  'Glucose': 166,
  'BloodPressure': 72,
  'SkinThickness': 19,
  'Insulin': 175,
  'BMI': 25.8,
  'DiabetesPedigreeFunction': 0.587,
  'Age': 51
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
