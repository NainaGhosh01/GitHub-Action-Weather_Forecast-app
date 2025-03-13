import requests
import logging
import os
from config import API_KEY  # Import API key from config.py

# Set up logging
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "weather.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to get weather data
def get_weather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        data = response.json()
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        logging.info(f"Weather fetched successfully for {city}")
        return weather_info

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather for {city}: {e}")
        return None

# Main function
def main():
    print("\nWelcome to Weather Forecast App!\n")
    
    while True:
        city = input("Enter city name: ").strip()
        
        if not city:
            print("City name cannot be empty. Please try again.")
            continue
        
        weather = get_weather(city)
        
        if weather:
            print(f"\nWeather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Condition: {weather['condition']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} km/h")
        else:
            print("\nError fetching weather. Please check your city name and try again.")
        
        another = input("\nWould you like to check another city? (yes/no): ").strip().lower()
        if another != "yes":
            print("Thank you for using the Weather Forecast App!")
            break

if __name__ == "__main__":
    main()
