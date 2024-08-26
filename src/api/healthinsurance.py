import pickle
import pandas as pd

class HealthInsuranceCrossSell:
    def __init__(self):
        self.home_path = '../features/'
        self.encoders = pickle.load(open(self.home_path + 'encoders.pkl', 'rb'))
        self.scalers = pickle.load(open(self.home_path + 'scalers.pkl', 'rb'))
        self.final_features = [
            'age', 'gender', 'famous_region', 'vehicle_damage', 'vehicle_age',
            'policy_sales_channel2_124','policy_sales_channel2_152', 
            'policy_sales_channel2_26'
            ]
        self.id = []
    
    def data_cleaning(self, df):
        # Filter who doesn't have driving license
        df = df[df['driving_license'] == 1].drop('driving_license', axis=1)

        # Saving id
        self.id = df['id'].values
        
        return df
        
    def feature_engineering(self, df):
        # Famous region
        df['famous_region'] = 0
        df.loc[df['region_code'] == 28, 'famous_region'] = 1

        # Policy sales channel 2
        df['policy_sales_channel2'] = df['policy_sales_channel'].copy().astype('int64').astype(str)
        df.loc[~df['policy_sales_channel'].isin([152, 26, 124]), 'policy_sales_channel2'] = 'others'

        # Vehicle age 2
        df['vehicle_age2'] = 0
        df.loc[df['vehicle_age'].isin(['1-2 Year', '> 2 Years']), 'vehicle_age2'] = 1

        # Famous policy sales channel
        df['famous_policy_sales_channel'] = 0
        df.loc[df['policy_sales_channel'].isin([152, 26, 124]), 'famous_policy_sales_channel'] = 1

        # Health insurance customer profitability
        df['hi_customer_profitability'] = df['annual_premium'].div(df['vintage']).fillna(0)
        
        return df

    def data_preparation(self, df):
        # Gender, vehicle damage, vehicle age and policy sales channel 2
        df = self.encoders.transform(df)
        df = pd.DataFrame(df, columns=self.encoders.get_feature_names_out())
        
        # Drop unnecessary features
        scaler_vars = [
            'id', 'age', 'vehicle_damage', 'annual_premium', 'vintage',
            'famous_region', 'vehicle_age', 'vehicle_age2', 
            'hi_customer_profitability', 'famous_policy_sales_channel', 
            'policy_sales_channel2_124', 'policy_sales_channel2_152', 
            'policy_sales_channel2_26', 'gender'
        ]

        df = df[scaler_vars]

        # Age
        df = self.scalers.transform(df)
        df = pd.DataFrame(df, columns=self.scalers.get_feature_names_out())

        # Selecting features
        df = df[self.final_features]
        return df
    
    def get_prediction(self, model, original_data, test_data):
        y_pred = model.predict(test_data)
        y_predict_proba = model.predict_proba(test_data)[:, 1]

        pred_df = pd.DataFrame(self.id, columns=['id'])
        pred_df['prediction'] = y_pred
        pred_df['probability'] = y_predict_proba

        original_data = original_data.merge(pred_df, on='id', how='left')

        # Driving license = 1 (data cleaning filter because of business question)
        original_data['prediction'] = original_data['prediction'].fillna(1)
        original_data['probability'] = original_data['probability'].fillna(0.9999)

        return original_data.to_json(orient='records', date_format='iso')