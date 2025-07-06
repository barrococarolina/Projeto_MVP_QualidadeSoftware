import requests

url = "http://localhost:5000/predict"

sample_input = {
    "school": "GP", "sex": "F", "age": 17, "address": "U", "famsize": "GT3", "Pstatus": "T",
    "Medu": 4, "Fedu": 4, "Mjob": "teacher", "Fjob": "teacher", "reason": "course", "guardian": "mother",
    "traveltime": 1, "studytime": 2, "failures": 0, "schoolsup": "no", "famsup": "yes", "paid": "no",
    "activities": "yes", "nursery": "yes", "higher": "yes", "internet": "yes", "romantic": "no",
    "famrel": 4, "freetime": 3, "goout": 4, "Dalc": 1, "Walc": 1, "health": 5, "absences": 2,
    "G1": 15, "G2": 14, "subject": "mat"
}

response = requests.post(url, json=sample_input)

print("Status code:", response.status_code)
print("Response:", response.json())