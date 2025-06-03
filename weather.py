import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n🌦️  Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    elif response.status_code == 404:
        print("❌ City not found. Please check the name and try again.")
    else:
        print("❌ Error fetching data. Please try again later.")

def main():
    with open("key.txt", "r") as file:
        api_key = file.read().strip()

    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
    
def main():
    with open("key.txt", "r") as file:
        api_key = file.read().strip()

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("👋 Exiting Weather App. Stay safe!")
            break
        elif city.strip() == '':
            print("⚠️  City name cannot be empty. Please enter a valid city.")
        else:
            get_weather(city, api_key)

if __name__ == "__main__":
    main()

