import pandas as pd
import json

df = pd.read_csv('C:/Users/juane/Taller1_Opportunity/Taller1_Opportunity/Dataset.csv')
df.to_json('Dataset.json', orient='records')
with open('Dataset.json', 'r') as file:
    data = json.load(file)
for i in range(100):
    data = data[i]
    print(data)
    break

    
