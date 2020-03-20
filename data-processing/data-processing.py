import requests
import pandas as pd
import io
import json

# Inputs
dataUrl = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data.csv'
savePath = '/Users/sandro.nunes/repos/covid19/data/data.json'

# Get Data
response = requests.get(dataUrl)
decodedResponse = response.content.decode('utf-8')
data = pd.read_csv(io.StringIO(decodedResponse))

# Save to JSON
dataJson = json.loads(data.to_json(orient='records'))
with open(savePath, 'w') as f:
    json.dump(dataJson, f)
