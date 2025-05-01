import requests

# real Render app URL
url = "https://p4-udacity-census-ml-api.onrender.com/predict"

payload = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 284582,
    "education": "Bachelors",
    "education-num": 13,
    "marital-status": "Never-married",
    "occupation": "Tech-support",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 50,
    "native-country": "United-States"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Prediction:", response.json())
