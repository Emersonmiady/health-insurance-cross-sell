import pandas as pd
from utils_rendler import upload_data

# Credentials
creds = {
'PG_DB': 'pa004_5sdi',
'PG_USER': 'meigabots',
'PG_HOST': 'dpg-cpcf43rtg9os738cbgvg-a.oregon-postgres.render.com',
'PG_PSWD': 'jHtR4eEQNDPquJjosnuZQ76KS6d1lMOT'
}

# Import pandas DataFrames
demographics = pd.read_csv("../../../data/external/demographics.csv").astype('object')
policy_and_response = pd.read_csv("../../../data/external/policy_and_response.csv").astype('object')
vehicle = pd.read_csv("../../../data/external/vehicle.csv").astype('object')

# Upload data
upload_data(creds, demographics, 'demographics')
print('demographics uploaded')
upload_data(creds, policy_and_response, 'policy_and_response')
print('policy_and_response uploaded')
upload_data(creds, vehicle, 'vehicle')
print('vehicle uploaded')

print('all data uploaded!')