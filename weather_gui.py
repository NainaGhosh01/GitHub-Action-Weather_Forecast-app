import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap API Key (Replace 'YOUR_API_KEY' with your actual key)
API_KEY = "ecc1e94412272560a6623f9d01291889"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = f"Weather in {data['name']}:\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Condition: {data['weather'][0]['description'].title()}\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} km/h"
        result_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found. Please try again.")

# Creating the GUI window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

# UI Components
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
