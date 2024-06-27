# Health Insurance Cross-Sell

## This project aims to order a potential client list by propensity score

#### This project was made by Emerson Hideki Miady.

# 1. Business Problem

Our client is an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.

An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.

For example, you may pay a premium of Rs. 5000 each year for a health insurance cover of Rs. 200,000/- so that if, God forbid, you fall ill and need to be hospitalised in that year, the insurance provider company will bear the cost of hospitalisation etc. for upto Rs. 200,000. Now if you are wondering how can company bear such high hospitalisation cost when it charges a premium of only Rs. 5000/-, that is where the concept of probabilities comes in picture. For example, like you, there may be 100 customers who would be paying a premium of Rs. 5000 every year, but only a few of them (say 2-3) would get hospitalised that year and not everyone. This way everyone shares the risk of everyone else.

Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer.

Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue. 

Now, in order to predict, whether the customer would be interested in Vehicle insurance, you have information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc.

Problem description on Kaggle: [click here](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction/data) to more information.

Note: the example has Rs. i.e. Rupee, an Indian money sign. So, the problem potentially is from an indian company.

# 2. Business Assumptions

- A crore (cr) denotes ten million and is equal to 100 lakh in the Indian numbering system. So 1 lakh is 100,000 rupees. This DataFrame I am assuming that it's from India, just because it's problem description

- The decision on the amount of health insurance to purchase should be based on a thorough evaluation of personal and family health needs, income levels, and potential future medical expenses

- For the insurance company, we have to maximize the LTV of the customers with the lowest probability of vehicle loss

# 3. Solution Strategy

- Granularity and problem type: ID classification of interested or not

- Potential solution methods: logistic regression, tree based models, KNN

- Delivery format:
    - Client prediction of interest on vehicle insurance
    - Possibility of *google sheets* to check the clients information and customize the priorization, not just by rank of customer profit

My strategy to solve this challenge was:

**Step 01. Data Description:**

|Variable|Definition|
|--------|----------|
|id|Unique ID for the customer|
|Gender|Gender of the customer|
|Age|Age of the customer|
|Driving_License|0 : Customer does not have DL, 1 : Customer already has DL|
|Region_Code|Unique code for the region of the customer|
|Previously_Insured|1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance|
|Vehicle_Age|Age of the Vehicle|
|Vehicle_Damage|1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.|
|Annual_Premium|The amount customer needs to pay as premium in the year|
|Policy_Sales_Channel|Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.|
|Vintage|Number of Days, Customer has been associated with the company|
|Response|1 : Customer is interested, 0 : Customer is not interested|

**Step 02. Feature Engineering:**

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Top 3 Data Insights

**Hypothesis 01:** If the car has been insured, then the customers will have more interest on the insurance of the company.

**FALSE.** If the car has been insured, the interest on vehicle insurance is **lower**. This is curious, maybe it is related with bad experiences with other vehicle insurance companies.

**Hypothesis 02:** If the vehicle was been damaged, then the vehicle insurance interest is greater.

**TRUE.** If the vehicle was been damaged, normally people want a vehicle insurance.

**Hypothesis 03:** Customers with older vehicle have less interest on vehicle insurance.

**FALSE.** Customers with older vehicle have **more interest** on vehicle insurance. This is curious too, people with less vehicle age tend to preserve their vehicles earlier...

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

# LICENSE

# All Rights Reserved - Comunidade DS 2021
