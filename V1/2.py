import pandas as pd


df = pd.read_csv('Ecommerce_Purchases.csv')
en = df[df['Language'] == 'en'].shape[0]

card_number = 4926535242672853
email = df[df['Credit Card'] == card_number]['Email'].values[0]

print(en)
print(email)