import streamlit as st
import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title("Weather App")
    st.markdown("Check the weather for your location")

    api_key = "YOUR_API_KEY"
    city = st.text_input("Enter your city")
    if st.button("Get Weather"):
        if city:
            weather_data = get_weather_data(city, api_key)
            if weather_data["cod"] == "404":
                st.error("City not found. Please enter a valid city name.")
            else:
                temperature = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                st.success(f"Weather in {city}:")
                st.write(f"Temperature: {temperature}°C")
                st.write(f"Description: {description}")
                st.write(f"Humidity: {humidity}%")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()

