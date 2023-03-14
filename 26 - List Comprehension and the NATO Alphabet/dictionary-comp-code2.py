weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
weather_f = {day: (c_deg * 9/5) + 32 for (day, c_deg) in weather_c.items()}

print(weather_f)
