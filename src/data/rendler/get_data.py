import pandas as pd
from utils_rendler import get_data

# Credentials
creds = {
    'PG_DB': 'pa004_5sdi',
    'PG_USER': 'meigabots',
    'PG_HOST': 'dpg-cpcf43rtg9os738cbgvg-a.oregon-postgres.render.com',
    'PG_PSWD': 'jHtR4eEQNDPquJjosnuZQ76KS6d1lMOT'
}

# Query to get data
query = '''
    SELECT
        d."ID" AS id, 
        d."GENDER" AS gender, 
        d."AGE" AS age, 
        v."DRIVING_LICENSE" AS driving_license, 
        d."REGION_CODE" AS region_code, 
        v."PREVIOUSLY_INSURED" AS previously_insured, 
        v."VEHICLE_AGE" AS vehicle_age, 
        v."VEHICLE_DAMAGE" AS vehicle_damage, 
        pr."ANNUAL_PREMIUM" AS annual_premium, 
        pr."POLICY_SALES_CHANNEL" AS policy_sales_channel, 
        pr."VINTAGE" AS vintage, 
        pr."RESPONSE" AS response
    FROM public.demographics d
    LEFT JOIN public.vehicle v ON (d."ID" = v."ID")
    LEFT JOIN public.policy_and_response pr ON (d."ID" = pr."ID")
'''

# Import data
df = get_data(creds, query)

# Save data
df.to_csv('../../../data/raw/health_insurance_cross_sell.csv', index=False)
print('data imported!')

