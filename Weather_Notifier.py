# Import the 'requests' library to make HTTP requests (to fetch weather and location data)
import requests  

# Import the 'notification' class from 'plyer' to show desktop notifications
from plyer import notification  

# Set the city for which we want to get the weather
city = "Delhi"  

# URL of the Open-Meteo Geocoding API (used to find latitude & longitude of the city)
geo_url = "https://geocoding-api.open-meteo.com/v1/search"  

# Parameters to pass to the API (search city name, return only 1 best match)
geo_params = {"name": city, "count": 1}  

# Send request to the geocoding API and get the response in JSON format
geo_res = requests.get(geo_url, params=geo_params).json()  

# Check if the API response contains "results" (i.e., city was found)
if "results" in geo_res:  
    # Extract latitude and longitude of the city from the API response
    lat = geo_res["results"][0]["latitude"]  
    lon = geo_res["results"][0]["longitude"]  

    # URL of the Open-Meteo Weather API
    weather_url = "https://api.open-meteo.com/v1/forecast"  

    # Parameters to pass to the weather API (latitude, longitude, current weather only)
    weather_params = {  
        "latitude": lat,  
        "longitude": lon,  
        "current_weather": True  
    }  

    # Send request to the weather API and get response in JSON format
    weather_res = requests.get(weather_url, params=weather_params).json()  

    # Print the entire weather response (for debugging purposes)
    print(weather_res)  

    # Check if current weather data is available in the response
    if "current_weather" in weather_res:  
        # Extract temperature and windspeed values
        temp = weather_res["current_weather"]["temperature"]  
        wind = weather_res["current_weather"]["windspeed"]  

        # Format the weather info in a user-friendly string
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"  

        # Print the formatted weather information
        print("Weather: ", weather_info)  

        # Show a desktop notification with the weather update
        notification.notify(  
            title="Weather Update",   # Title of the notification
            message=weather_info,     # Message body of the notification
            timeout=5                 # Notification disappears after 5 seconds
        )  
    else:  
        # If no weather data found for the city
        print("Weather data not found")  
else:  
    # If the city is not found in the geocoding API
    print("City not Found")  
