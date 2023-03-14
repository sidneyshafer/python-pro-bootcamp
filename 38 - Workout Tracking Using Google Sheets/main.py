import requests
from datetime import datetime

APP_ID = "fa1b1acf"
API_KEY = "0fdca4d3d522d43b9b3f6ef8da8c215c"

GENDER = "female"
WEIGHT_KG = 47.63
HEIGHT_CM = 162.56
AGE = 18

USERNAME = "Sidney_Shafer"
PASSWORD = "Donuts!1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e78924113f957b2052e64de7c17793ea/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


# Basic Authentication
sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(USERNAME, PASSWORD,)
)

