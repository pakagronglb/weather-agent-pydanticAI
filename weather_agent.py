""" Pydantic AI Weather Agent Example """
import os
from typing import Any
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry, RunContext
from load_models import OPENAI_MODEL
from dotenv import load_dotenv
import requests

load_dotenv()

class Deps(BaseModel):
    """ Default Dependencies """
    weather_api_key: str | None = Field(title='Weather API Key', description='weather service API key')
    geo_api_key: str | None = Field(title='Geo API Key', description='geo service API key')

class WeatherResponse(BaseModel):
    """Response type for weather information"""
    message: str = Field(description="Weather information message")

weather_agent = Agent(
    name='Weather Agent',
    model=OPENAI_MODEL,
    system_prompt=(
        'Be concise, reply with one sentence. '
        'Use the `get_lat_lng` tool to get the latitude and longitude of the locations, '
        'then use the `get_weather` tool to get the weather.'
    ),
    deps_type=Deps,
    result_type=WeatherResponse,
)

@weather_agent.tool
def get_lat_lng(
    ctx: RunContext[Deps], location_description: str
) -> dict[str, float]:
    """Get the latitude and longitude of a location."""
    base_url = "https://api.geoapify.com/v1/geocode/search"
    params = {
        'text': location_description,
        'apiKey': ctx.deps.geo_api_key,
        'format': 'json'
    }
    
    print(f'Looking up coordinates for: {location_description}')
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['results'] and len(data['results']) > 0:
            location = data['results'][0]
            result = {
                'lat': location['lat'],
                'lng': location['lon']
            }
            print(f'Found coordinates for {location_description}: {result}')
            return result
    
    raise ModelRetry(f'Could not find the location: {location_description}')
    
@weather_agent.tool
def get_weather(ctx: RunContext[Deps], lat: float, lng: float) -> dict[str, Any]:
    """Get the weather at a location.

    Args:
        ctx: The context.
        lat: The latitude of the location.
        lng: The longitude of the location.
    """
    if lat == 0 and lng == 0:
        raise ModelRetry('Could not find the location')

    print(f'Getting weather for coordinates: lat={lat}, lng={lng}')
    params = {
        'lat': lat,
        'lng': lng,
        'api_key': ctx.deps.weather_api_key,
    }
    # Simulate an API call to get the weather info
    if lat == 10.79532 and lng == -55.393958:
        result = {'temp': 70, 'description': 'Snowing'}
        print(f'Weather at coordinates: {result}')
        return result
    elif lat == 37.7749 and lng == -122.4194:
        result = {'temp': 100, 'description': 'Windy'}
        print(f'Weather at coordinates: {result}')
        return result
    
if __name__ == '__main__':
    deps = Deps(
        weather_api_key=os.getenv('WEATHER_API_KEY'),
        geo_api_key=os.getenv('GEO_API_KEY')
    )
    
    result = weather_agent.run_sync(
        'What is the weather like in London and in San Francisco, CA?',
        deps=deps
    )

    print('---')
    print('Result:')
    print(result.data.message)