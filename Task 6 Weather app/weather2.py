import tkinter as tk
import requests
import csv

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = tk.Label(root, text="Enter City Name:")
        self.location_label.pack()

        self.location_entry = tk.Entry(root)
        self.location_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather Info", command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_display_label = tk.Label(root, text="")
        self.weather_display_label.pack()

    def get_weather(self):
        location = self.location_entry.get()
        if location:
            weather_data = self.fetch_weather_data(location)
            if weather_data:
                weather_info = self.parse_weather_data(weather_data)
                self.display_weather_info(weather_info)
                self.save_weather_data_to_csv(location, weather_info)
            else:
                self.weather_display_label.config(text="Failed to fetch weather data.")
        else:
            self.weather_display_label.config(text="Please enter a location.")

    def fetch_weather_data(self, location):
        api_key = "572e804927911fd31d4552a21ac74638"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def parse_weather_data(self, weather_data):
        weather_info = {
            "Temperature": weather_data["main"]["temp"],
            "Humidity": weather_data["main"]["humidity"],
            "Description": weather_data["weather"][0]["description"]
        }
        return weather_info

    def display_weather_info(self, weather_info):
        text = f"Temperature: {weather_info['Temperature']}°C\n"
        text += f"Humidity: {weather_info['Humidity']}%\n"
        text += f"Weather: {weather_info['Description']}"
        self.weather_display_label.config(text=text)

    def save_weather_data_to_csv(self, location, weather_info):
        filename = "weather_data.csv"
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([location, weather_info["Temperature"], weather_info["Humidity"], weather_info["Description"]])
        print("Weather data saved to CSV file.")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
