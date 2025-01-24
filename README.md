
# Weather Agent with Pydantic AI

This project demonstrates a smart weather agent built using Pydantic AI that combines geocoding (Geoapify) and weather data (OpenWeather) to provide weather information for different locations.

## Features

- Location to coordinates conversion using Geoapify API
- Weather information retrieval using OpenWeather API
- Natural language processing using OpenAI's GPT models
- Type-safe API interactions using Pydantic models


## Installation

# Prerequisites

- Python 3.8+
- API keys for:
  - OpenAI
  - Geoapify (get it from [Geoapify](https://www.geoapify.com/))
  - OpenWeather (get it from [OpenWeather](https://openweathermap.org/api))
  - Pydantic AI

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-agent
```

2. Create a virtual environment and activate it:
```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
```bash
pip install pydantic-ai python-dotenv openai requests
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
```sh
    OPENAI_API_KEY=your_openai_api_key
GEO_API_KEY=your_geo_api_key  WEATHER_API_KEY=your_weather_api_key
```


## Usage/Examples

To use the weather agent, simply run `python weather_agent.py` script. The agent will fetch weather information for specified locations using the provided API keys.

## API Reference

### Geoapify API
- Used for geocoding (converting location names to coordinates)
- Endpoint: `https://api.geoapify.com/v1/geocode/search`
- Documentation: [Geoapify Geocoding API](https://www.geoapify.com/geocoding-api)
- Required parameters:
  - `text`: Location description
  - `apiKey`: Your Geoapify API key
  - `format`: Response format (json)

### OpenWeather API
- Used for weather information
- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Documentation: [OpenWeather API](https://openweathermap.org/current)
- Required parameters:
  - `lat`: Latitude
  - `lon`: Longitude
  - `appid`: Your OpenWeather API key

## Code Examples

### Getting Coordinates (Geoapify)
```python
response = requests.get(
"https://api.geoapify.com/v1/geocode/search",
params={
'text': 'London',
'apiKey': 'your_api_key',
'format': 'json'
}
)
```

### Getting Weather (OpenWeather)
```python
"https://api.openweathermap.org/data/2.5/weather",
params={
'lat': 51.5074,
'lon': -0.1278,
'appid': 'your_api_key',
'units': 'metric'
}
)
```


## Error Handling

The agent includes error handling for:
- Invalid locations
- API rate limits
- Network errors
- Missing API keys

## Contributing

Contributions are always welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request



## License

This project is licensed under the MIT License - see the LICENSE file for details.



## Acknowledgements

- [Pydantic AI](https://github.com/jxnl/pydantic-ai)
- [Geoapify](https://www.geoapify.com/)
- [OpenWeather](https://openweathermap.org/)
