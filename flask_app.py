from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)

     for col in model_columns:
          if col not in query.columns:
               query[col] = 0

     prediction = rf.predict(query)
     return jsonify({'prediction': list(prediction.tolist())})

if __name__ == '__main__':
     rf = joblib.load('/home/aorso/Documents/github/kaggle_hr_analytics/rf.pkl')
     model_columns = joblib.load('/home/aorso/Documents/github/kaggle_hr_analytics/rf_columns.pkl')
     app.run(port=8080, debug = True)



