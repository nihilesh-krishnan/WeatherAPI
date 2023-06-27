    import requests
    from bs4 import BeautifulSoup

    city = input("Enter the city name: ")
    search = f"weather in {city}"
    url = f"https://www.google.com/search?q={search}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        temperature_celsius = float(soup.find("span", class_="wob_t").text)
        temperature_fahrenheit = round((temperature_celsius * 9/5) + 32, 2)
        print(f"The current temperature in {city} is {temperature_fahrenheit} °F")
    except requests.exceptions.RequestException:
        print("Failed to retrieve weather information.")
