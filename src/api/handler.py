import pandas as pd
import pickle
import requests
from flask import Flask, request, Response
from healthinsurance import HealthInsuranceCrossSell

def transform_column(column, transformation_dict):
    '''
    Transforms a column using a dictionary of transformations
    '''
    return column.map(transformation_dict).values.reshape(-1, 1)

app = Flask(__name__)

path = '../model/'
model = pickle.load(open(path + 'best-model.pkl', 'rb'))

@app.route('/healthinsurance/predict', methods=['POST'])
def healthinsurance_predict():
    test_json = request.get_json()

    if test_json: # there is data
        if isinstance(test_json, dict): # unique sample
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else: # multiple samples
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instantiate HealthInsuranceCrossSell class
        pipeline = HealthInsuranceCrossSell()

        # Data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # Feature engineering
        df2 = pipeline.feature_engineering(df1)

        # Data preparation
        df3 = pipeline.data_preparation(df2)

        # Prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response
    
    else:
        return Response('{}', status=200, mimetype='aplication/json')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)