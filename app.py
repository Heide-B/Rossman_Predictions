from flask import Flask, jsonify, make_response, request, abort
import pandas as pd
from preprocess import *
import catboost
import joblib

model = joblib.load(open( "pred_model2.joblib", "rb"))
store = pd.read_csv('store.csv')
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/")
def hello():
  return "You can find the code in this repository https://github.com/Heide-B/Rossman_Predictions. \nThe URL to call predictions is /predict/!"

@app.route("/predict", methods=['POST'])
def get_prediction():
    if not request.json:
        abort(400)
    df = pd.DataFrame(request.json, index=[0])
    df = df.merge(store, on='Store',how='inner')
    inputs = preprocess(df)
    return jsonify({'sales': "{:.2f}".format(model.predict(inputs)[0])}), 201

if __name__ == "__main__":
  app.run()