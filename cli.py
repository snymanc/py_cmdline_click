import os
import click
import requests


@click.group()
def main():
    pass


def current_weather(location, api_key):
    url = 'http://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']


@main.command()
@click.argument('location')
@click.option(
    '--api-key', '-a',
    envvar="API_KEY",
    help='your API key for the OpenWeatherMap API',
)
def current(location, api_key):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. London,UK

    2. Johannesburg

    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    weather = current_weather(location, api_key)
    print(f"The weather in {location} right now: {weather}.")


@main.command()
@click.option(
    '--api-key', '-a',
    help='your API key for the OpenWeatherMap API',
)
def config(api_key):
    """
    Store configuration values in a file.
    """
    config_file = os.path.expanduser('.weather.cfg')

    api_key = click.prompt("Please enter your API key?", default=api_key)

    with open(config_file, 'w') as cfg:
        cfg.write(api_key)


if __name__ == "__main__":
    main()
