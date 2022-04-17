import requests
from datetime import datetime

GENDER = 'male'
WEIGHT = 55
HEIGHT = 1.78
AGE = 21

NUTRITIONIX_API_ID = 'bf865b2b'
NUTRITIONIX_API_KEY = '40637d1482a7689495f3c6c8aff2a798'

ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input("Tell me which exercises you did: ")

GET = 'https://api.sheety.co/f19dc6e67d09e295a33f440f8fcff01d/myWorkouts/workouts'
POST = 'https://api.sheety.co/f19dc6e67d09e295a33f440f8fcff01d/myWorkouts/workouts'

headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(ENDPOINT, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(POST, json=sheet_inputs, auth=('bryansandoval', 'lalasemia2'))

    print(sheet_response.text)
