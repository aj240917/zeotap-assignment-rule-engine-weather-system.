def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def send_alert(city, temperature):
    print(f"Alert: The temperature in {city} has exceeded the threshold! Current temperature: {temperature:.2f}°C")
    # You can implement email or SMS notifications here if needed.
