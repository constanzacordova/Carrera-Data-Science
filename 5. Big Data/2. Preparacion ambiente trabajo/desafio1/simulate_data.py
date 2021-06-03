#simulate_data.py
from random import seed
import numpy as np
import csv

def create_random_row(supress_target = False):
    deliverer_id = np.random.choice(range(100), 1)[0]
    delivery_zone = np.random.choice(['I', 'II', 'III', 'IV','V', 'VI', 'VII', 'VIII'])
    monthly_app_usage = np.random.poisson(15)
    subscription_type = np.random.choice(['Free','Prepaid','Monthly', 'Trimestral','Semestral', 'Yearly'], 1, [.30, .20, 10, .15, .20, .05])[0]
    paid_price = np.random.normal(25.45, 10)
    customers_size = np.random.poisson(2) + 1
    menu = np.random.choice(['Asian', 'Indian','Italian', 'Japanese','French', 'Mexican'],1)[0]
    delay_time = np.random.normal(10, 3.2)

    if supress_target is True:
        tmp_array = [deliverer_id, delivery_zone, subscription_type, monthly_app_usage, customers_size, paid_price, menu]
    
    else:
        tmp_array = [deliverer_id, delivery_zone, subscription_type, monthly_app_usage, customers_size, paid_price, menu, delay_time]

    return tmp_array

# generate train_delivery_data.csv
with open('train_delivery_data.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    np.random.seed(11238)

    for i in range(1000):
        file.writerow(create_random_row())

# generate test_delivery_data.csv
with open('test_delivery_data.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    np.random.seed(42)

    for i in range(10000):
        file.writerow(create_random_row(supress_target=True))