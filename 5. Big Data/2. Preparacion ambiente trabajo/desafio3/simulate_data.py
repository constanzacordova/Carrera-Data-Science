import random
import numpy as np
import csv


def crear_filas():
    deliverer_id  = np.random.choice(range(100), 1)[0]
    delivery_zone = np.random.choice(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'])
    monthly_app_usage = np.random.poisson(15)
    subscription_type = np.random.choice(['Free','Prepaid','Monthly', 'Trimestral', 'Semestral', 'Yearly'], 1,[.30, .20, 10, .15, .20, .05])[0]
    paid_price = np.random.normal(25.45, 10)
    customer_size = np.random.poisson(2) + 1
    menu = np.random.choice(['Asian', 'Indian', 'Italian', 'Japanese','French', 'Mexican'],1)[0]
    delay_time = np.random.normal(10,3.2)

    return [deliverer_id, delivery_zone, monthly_app_usage, subscription_type, paid_price, customer_size, menu, delay_time]

with open(f"train_delivery_data.csv", 'w') as csvfile:
    np.random.seed(11238)
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for _ in range(1000):
        file.writerow(crear_filas())
print("Listo train!")

with open(f"test_delivery_data.csv", 'w') as csvfile:
    np.random.seed(42)
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for _ in range(10000):
        file.writerow(crear_filas())

print("Listo test!")

